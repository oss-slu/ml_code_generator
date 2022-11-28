import os
import json

from flask import g
from flask import current_app
from flask import render_template
from flask import request, redirect, flash
from flask import session
from flask import jsonify

from werkzeug.utils import secure_filename

from flask_app.api.generator import generator
from flask_app.api.utils import allowed_file
from flask_app.api.map_paths import correct_action

def welcome():
   session['current_state'] = 'start'
   return render_template('home.html')

def makeIpynb(code):
   template = {"cells":[{"cell_type":"code","metadata":{},"outputs":[],"source":[code]}],"metadata":{"language_info":{"name":"python"},"orig_nbformat":4},"nbformat":4,"nbformat_minor":2}
   with open ("data/sample.ipynb", "w") as outfile:
      json.dump(template,outfile)
 
def download_code():
   session['current_state'] = 'download'
   code = generator.download_code()
   makeIpynb(code)
   return render_template('info/code.html', text=code)

def describe_data():
   session['current_state'] = 'describe'
   description = generator.describe_data()
   return render_template('info/description.html', table=description.to_html())

def clean_data():
   session['current_state'] = 'clean'
   generator.clean_data()
   #return render_template('info/cleaning_summary.html', removed_rows=num_rows_removed)

def split_data():
   session['current_state'] = 'split'
   if request.method == 'POST':
      request_dict = request.form.to_dict()
      training_ratio = int(request_dict['trainingRatioRange'])/100
      train_data_size = generator.split_data(training_ratio)
      return render_template('info/splitting_summary.html', num_rows_train=train_data_size[0])

   return render_template('actions/select_training_ratio_value.html')

def select_features():
   session['current_state'] = 'prepare'
   if request.method == 'POST':
      request_dict = request.form.to_dict(flat=False)
      generator.drop_x(request_dict['drop_labels'])
      clean_data()
      return redirect('/select_y')

   keys = generator.get_labels()
   return render_template('actions/select_input_values.html', labels=keys)

def select_y():
   session['current_state'] = 'prepare'
   if request.method == 'POST':
      request_dict = request.form.to_dict()
      generator.select_y(request_dict['label'])
      return redirect('/split?')

   keys = generator.get_labels()
   return render_template('actions/select_output_value.html', labels=keys)
   # return render_template('labels.html', labels=keys)

def upload_file():
   session['current_state'] = 'upload'
   if request.method == 'POST':
      # check if the post request has the file part
      if 'file' not in request.files:
         flash('No file part')
         return redirect(request.url)

      file = request.files['file']
      # If the user does not select a file, the browser submits an
      # empty file without a filename.
      if file.filename == '':
         flash('No selected file')
         return redirect(request.url)

      if file and allowed_file(file.filename):
         filename = secure_filename(file.filename)
         file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
         # return redirect(url_for('download_file', name=filename))
         print(g)

         with current_app.app_context():
            generator.load_data(current_app.config['UPLOAD_FOLDER']+'/' + filename)

         return redirect('/describe')

   return render_template('actions/upload_data.html')

def train_model():
   session['current_state'] = 'train'
   generator.train_model()
   return download_code()

def next_actions():
   return correct_action(session['current_state'])

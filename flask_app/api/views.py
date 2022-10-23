import os

from flask import g
from flask import current_app
from flask import render_template
from flask import request, redirect, flash
from werkzeug.utils import secure_filename

from flask_app.api.generator import get_generator
from flask_app.api.utils import allowed_file


def welcome():
   return render_template('home.html')

def download_code():
   code = get_generator().download_code()
   return render_template('info/code.html', text=code)

def describe_data():
   description = get_generator().describe_data()
   return render_template('info/description.html', table=description.to_html())

def clean_data():
   original_data_size = get_generator().get_data().shape
   cleaned_data_size = get_generator().clean_data()
   num_rows_removed = original_data_size[0]-cleaned_data_size[0]
   return render_template('info/cleaning_summary.html', removed_rows=num_rows_removed)

def split_data():
   if request.method == 'POST':
      request_dict = request.form.to_dict()
      training_ratio = int(request_dict['trainingRatioRange'])/100
      train_data_size = get_generator().split_data(training_ratio)
      return render_template('info/splitting_summary.html', num_rows_train=train_data_size[0])

   return render_template('actions/select_training_ratio_value.html')

def get_input_labels():
   if request.method == 'POST':
      request_dict = request.form.to_dict(flat=False)
      get_generator().drop_x(request_dict['drop_labels'])
      return render_template('actions/actions.html')

   keys = get_generator().get_labels()
   return render_template('actions/select_input_values.html', labels=keys)

def get_data_labels():
   if request.method == 'POST':
      request_dict = request.form.to_dict()
      get_generator().select_y(request_dict['label'])
      return redirect('/input_labels')

   keys = get_generator().get_labels()
   return render_template('actions/select_output_value.html', labels=keys)
   # return render_template('labels.html', labels=keys)

def upload_file():
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
            get_generator().load_data(current_app.config['UPLOAD_FOLDER']+'/' + filename)

         return render_template('actions/actions.html')

   return render_template('actions/upload_data.html')

def train_model():
   get_generator().train_model()
   return download_code()

def next_actions():
   return render_template('actions/actions.html')

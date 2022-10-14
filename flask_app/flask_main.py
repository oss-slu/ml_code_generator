import os

from flask import g
from flask import Flask
from flask import render_template
from flask import request, redirect, flash
from werkzeug.utils import secure_filename

from application import code_generator
from pandas_code.mapping import template_mapping
from pandas_code.parse_template import parse_template


ALLOWED_EXTENSIONS = {'csv'}

UPLOAD_FOLDER='data/'

def create_app():

   app = Flask(__name__, template_folder='templates')
   app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
   generator = code_generator.CodeGenerator(template_mapping, parse_template)

   @app.route('/')
   def welcome():
      return render_template('home.html')

   def allowed_file(filename):
      return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

   @app.route('/download', methods=['GET'])
   def download_code():
      code = generator.download_code()
      return render_template('info/code.html', text=code)

   @app.route('/describe', methods=['GET'])
   def describe_data():
      description = generator.describe_data()
      return render_template('info/description.html',table=description.to_html())

   @app.route('/clean', methods=['GET'])
   def clean_data():
      original_data_size = generator.get_data().shape
      cleaned_data_size = generator.clean_data()
      num_rows_removed = original_data_size[0]-cleaned_data_size[0]
      return render_template('info/cleaning_summary.html', removed_rows=num_rows_removed)

   @app.route('/split', methods=['GET', 'POST'])
   def split_data():
      if request.method == 'POST':
         request_dict = request.form.to_dict()
         training_ratio = int(request_dict['trainingRatioRange'])/100
         train_data_size = generator.split_data(training_ratio)
         return render_template('info/splitting_summary.html', num_rows_train=train_data_size[0])

      return render_template('actions/select_training_ratio_value.html')

   @app.route('/train', methods=['GET'])
   def train_model():
      trained_model = generator.train_model()
      return render_template('actions/train_model.html', trained=trained_model)

   @app.route('/input_labels', methods=['GET', 'POST'])
   def get_input_labels():
      if request.method == 'POST':
         request_dict = request.form.to_dict(flat=False)
         generator.drop_x(request_dict['drop_labels'])
         return render_template('actions/actions.html')

      keys = generator.get_labels()
      return render_template('actions/select_input_values.html', labels=keys)

   @app.route('/labels', methods=['GET', 'POST'])
   def get_data_labels():
      if request.method == 'POST':
         request_dict = request.form.to_dict()
         generator.select_y(request_dict['label'])
         return redirect('/input_labels')

      keys = generator.get_labels()
      return render_template('actions/select_output_value.html', labels=keys)
   #   return render_template('labels.html', labels=keys)

   @app.route('/data', methods=['GET', 'POST'])
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))
            print(g)
            with app.app_context():
               generator.load_data(app.config['UPLOAD_FOLDER']+'/'+filename)
            return render_template('actions/actions.html')

      return render_template('actions/upload_data.html')

   @app.route('/actions')
   def next_actions():
      return render_template('actions/actions.html')

   return app

# main driver function
if __name__ == '__main__':
   # run() method of Flask class runs the application
   # on the local development server.
   main_app = create_app()
   main_app.run()

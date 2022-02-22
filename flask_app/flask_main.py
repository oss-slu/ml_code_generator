import os

from flask import g
from flask import Flask
from flask import render_template
from flask import request, redirect, flash
from werkzeug.utils import secure_filename

from application import code_generator

ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
UPLOAD_FOLDER='../data/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
generator = code_generator.CodeGenerator()

@app.route('/')
def welcome():
   return render_template('base.html')

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/download', methods=['GET'])
def download_code():
   code = generator.download_code()
   return render_template('code.html', text=code)

@app.route('/describe', methods=['GET'])
def describe_data():
   description = generator.describe_data()
   return render_template('description.html',table=description.to_html())

@app.route('/clean', methods=['GET'])
def clean_data():
   original_data_size = generator.dataframe.shape
   cleaned_data_size = generator.clean_data()
   num_rows_removed = original_data_size[0]-cleaned_data_size[0]
   return render_template('cleaning_summary.html', removed_rows=num_rows_removed)

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
         return render_template('actions.html')

   return render_template('upload_data.html')

@app.route('/actions')
def next_actions():
   return render_template('actions.html')

# main driver function
if __name__ == '__main__':
   # run() method of Flask class runs the application
   # on the local development server.
   app.run()

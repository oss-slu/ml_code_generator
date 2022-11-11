import os
from flask import Flask

from flask_app.api import views
from flask_app.api import google_auth

from flask_app.api.config import UPLOAD_FOLDER
from flask_app.api.config import GOOGLE_CLIENT_ID
from flask_app.api.config import GOOGLE_CLIENT_SECRET
from flask_app.api.config import GOOGLE_DISCOVERY_URL

def create_app():

   app = Flask(__name__, template_folder='templates')
   app.secret_key = os.urandom(24)
   # add config variables
   app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

   app.config['GOOGLE_CLIENT_ID'] = GOOGLE_CLIENT_ID
   app.config['GOOGLE_CLIENT_SECRET'] = GOOGLE_CLIENT_SECRET
   app.config['GOOGLE_DISCOVERY_URL'] = GOOGLE_DISCOVERY_URL

   # add routes
   app.add_url_rule('/', view_func=views.welcome, methods=['GET'])
   app.add_url_rule('/download', view_func=views.download_code, methods=['GET'])
   app.add_url_rule('/describe', view_func=views.describe_data, methods=['GET'])
   app.add_url_rule('/clean', view_func=views.clean_data, methods=['GET'])
   app.add_url_rule('/split', view_func=views.split_data, methods=['GET', 'POST'])
   app.add_url_rule('/train', view_func=views.train_model, methods=['GET'])
   app.add_url_rule('/input_labels', view_func=views.get_input_labels, methods=['GET', 'POST'])
   app.add_url_rule('/labels', view_func=views.get_data_labels, methods=['GET', 'POST'])
   app.add_url_rule('/data', view_func=views.upload_file, methods=['GET', 'POST'])
   app.add_url_rule('/actions', view_func=views.next_actions, methods=['GET'])
   app.add_url_rule('/login', view_func=authentication.login, methods=['GET'])
   app.add_url_rule('/login/callback', view_func=authentication.login_callback, methods=['GET'])
   return app

# main driver function
if __name__ == '__main__':
   # run() method of Flask class runs the application
   # on the local development server.
   main_app = create_app()
   main_app.run()

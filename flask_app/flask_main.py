import os
from flask import Flask

from flask_app.api import config
from flask_app.api import views
from flask_app.api.google_colab import google_auth
from flask_app.api.google_colab import google_drive

def create_app():

   app = Flask(__name__, template_folder='templates')
   app.secret_key = os.urandom(24)

   # add config variables
   config.load(app)

   # add routes
   app.add_url_rule('/', view_func=views.welcome, methods=['GET'])
   app.add_url_rule('/download', view_func=views.download_code, methods=['GET'])
   app.add_url_rule('/describe', view_func=views.describe_data, methods=['GET'])
   app.add_url_rule('/split', view_func=views.split_data, methods=['GET', 'POST'])
   app.add_url_rule('/train', view_func=views.train_lin_reg, methods=['GET'])
   app.add_url_rule('/select_features', view_func=views.select_features, methods=['GET', 'POST'])
   app.add_url_rule('/select_y', view_func=views.select_y, methods=['GET', 'POST'])
   app.add_url_rule('/continuous', view_func=views.continuous, methods=['GET', 'POST'])
   app.add_url_rule('/categorical', view_func=views.categorical, methods=['GET', 'POST'])
   app.add_url_rule('/data', view_func=views.upload_file, methods=['GET', 'POST'])
   app.add_url_rule('/actions', view_func=views.next_actions, methods=['GET'])
   app.add_url_rule('/login', view_func=google_auth.login, methods=['GET'])
   app.add_url_rule('/login/callback', view_func=google_auth.login_callback, methods=['GET'])
   app.add_url_rule('/upload', view_func=google_drive.upload, methods=['GET','POST'])
   app.add_url_rule('/download_code', view_func=google_drive.download, methods=['GET'])
   return app

# main driver function
# run() method of Flask class runs the application
# on the local development server.

main_app = create_app()

if __name__ == '__main__':
   main_app.run()

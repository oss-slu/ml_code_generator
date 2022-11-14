import os
from flask import Flask
from flask_app.api import views
from flask_app.api import google_auth
from flask_app.api import google_drive
from flask_app.api.config  import UPLOAD_FOLDER
from flask_app.api.config  import GOOGLE_CLIENT_ID
from flask_app.api.config   import GOOGLE_CLIENT_SECRET
from flask_app.api.config  import GOOGLE_DISCOVERY_URL

#os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

def create_app():
   app = Flask(__name__, template_folder='templates')
   app.secret_key = os.urandom(24)
   app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
   app.config['GOOGLE_CLIENT_ID'] = GOOGLE_CLIENT_ID
   app.config['GOOGLE_CLIENT_SECRET'] = GOOGLE_CLIENT_SECRET
   app.config['GOOGLE_DISCOVERY_URL'] = GOOGLE_DISCOVERY_URL
   # add routes
   app.add_url_rule('/', view_func=views.welcome, methods=['GET'])
   app.add_url_rule('/login', view_func=google_auth.login, methods=['GET'])
   app.add_url_rule('/login/callback', view_func=google_auth.login_callback, methods=['GET'])
   app.add_url_rule('/upload', view_func=google_drive.upload, methods=['GET', 'POST'])
   return app

if __name__ == "__main__":
   main_app = create_app()
   main_app.run(debug = True)

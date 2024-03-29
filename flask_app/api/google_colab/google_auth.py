from flask import current_app
from flask import url_for
from flask import session
from flask import redirect
import googleapiclient.discovery
import google.oauth2.credentials

import flask
from authlib.integrations.flask_client import OAuth

oauth = OAuth(current_app)

AUTH_TOKEN_KEY = 'auth_token'
AUTHORIZATION_SCOPE ='openid email profile https://www.googleapis.com/auth/drive.file'

app = flask.Blueprint('google_auth', __name__)

def build_credentials():
   return google.oauth2.credentials.Credentials(
               session['access_token'],
               client_id=current_app.config['GOOGLE_CLIENT_ID'],
               client_secret=current_app.config['GOOGLE_CLIENT_SECRET'],
               token_uri=current_app.config['ACCESS_TOKEN_URI'])

def get_user_info():
   credentials = build_credentials()

   oauth2_client = googleapiclient.discovery.build(
                        'oauth2', 'v2',
                        credentials=credentials)

   # pylint: disable=maybe-no-member
   return oauth2_client.userinfo().get().execute()

def login():
   oauth.register(
      name='google',
      client_id=current_app.config['GOOGLE_CLIENT_ID'],
      client_secret=current_app.config['GOOGLE_CLIENT_SECRET'],
      server_metadata_url=current_app.config['GOOGLE_DISCOVERY_URL'],
      client_kwargs={
         'scope': 'openid email profile https://www.googleapis.com/auth/drive.file'
      }
   )
   redirect_uri = url_for('login_callback', _external=True)
   return oauth.google.authorize_redirect(redirect_uri)

def login_callback():
   token=oauth.google.authorize_access_token()
   session['userinfo']=token['userinfo']
   session['access_token']=token['access_token']
   return redirect('/upload')

def is_logged_in():
   return bool(session['access_token'] in flask.session.values())

from flask import current_app
from flask import url_for
from flask import session
from flask import redirect

from authlib.integrations.flask_client import OAuth

oauth = OAuth(current_app)

def login():
   oauth.register(
      name='google',
      client_id=current_app.config['GOOGLE_CLIENT_ID'],
      client_secret=current_app.config['GOOGLE_CLIENT_SECRET'],
      server_metadata_url=current_app.config['GOOGLE_DISCOVERY_URL'],
      client_kwargs={
         'scope': 'openid email profile'
      }
   )
   redirect_uri = url_for('login_callback', _external=True)
   return oauth.google.authorize_redirect(redirect_uri)

def login_callback():
   token=oauth.google.authorize_access_token()
   session['userinfo']=token['userinfo']
   session['access_token']=token['access_token']
   return redirect('/')

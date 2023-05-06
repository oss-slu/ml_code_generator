import os
from dotenv import load_dotenv

ALLOWED_EXTENSIONS = {'csv'}
UPLOAD_FOLDER = 'data/'
GOOGLE_DISCOVERY_URL = 'https://accounts.google.com/.well-known/openid-configuration'
ACCESS_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'

def load(app):
   basedir = os.environ.get("PYTHONPATH", None)
   # read in environment variables
   #basedir = os.path.abspath(os.path.dirname(__file__))
   load_dotenv(os.path.join(basedir, '.env'))

   GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
   GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
   app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
   app.config['GOOGLE_CLIENT_ID'] = GOOGLE_CLIENT_ID
   app.config['GOOGLE_CLIENT_SECRET'] = GOOGLE_CLIENT_SECRET
   app.config['GOOGLE_DISCOVERY_URL'] = GOOGLE_DISCOVERY_URL
   app.config['ACCESS_TOKEN_URI'] = ACCESS_TOKEN_URI


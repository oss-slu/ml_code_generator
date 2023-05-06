import os
from dotenv import load_dotenv

ALLOWED_EXTENSIONS = {'csv'}
UPLOAD_FOLDER = 'data/'
GOOGLE_DISCOVERY_URL = 'https://accounts.google.com/.well-known/openid-configuration'
ACCESS_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'

def load(app):

   app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
   app.config['GOOGLE_DISCOVERY_URL'] = GOOGLE_DISCOVERY_URL
   app.config['ACCESS_TOKEN_URI'] = ACCESS_TOKEN_URI

   # load the .env file from the base directory
   basedir = os.environ.get("PYTHONPATH", None)
   # read in environment variables
   load_dotenv(os.path.join(basedir, '.env'))

   google_client_id = os.environ.get("GOOGLE_CLIENT_ID", None)
   google_client_secret = os.environ.get("GOOGLE_CLIENT_SECRET", None)
   # the client id and secret are intentionally not defined as global variables
   # they are loaded from the .env file in the base directory (basedir)
   # basedir is defined dynamically based on PYTHONPATH
   app.config['GOOGLE_CLIENT_ID'] = google_client_id
   app.config['GOOGLE_CLIENT_SECRET'] = google_client_secret


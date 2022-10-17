import os
from dotenv import load_dotenv

ALLOWED_EXTENSIONS = {'csv'}
UPLOAD_FOLDER = 'data/'

# read in environment variables
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = 'https://accounts.google.com/.well-known/openid-configuration'

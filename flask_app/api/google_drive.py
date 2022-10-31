import io
import tempfile

import flask

from apiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
import googleapiclient.discovery
from google_auth import build_credentials, get_user_info

from werkzeug.utils import secure_filename

app = flask.Blueprint('google_drive', __name__)

def build_drive_api_v3():
    credentials = build_credentials()
    return googleapiclient.discovery.build('drive', 'v3', credentials=credentials).files()
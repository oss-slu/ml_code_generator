import io
import tempfile

import flask
import flask_app.api.google_auth
from apiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
import googleapiclient.discovery
from werkzeug.utils import secure_filename

app = flask.Blueprint('google_drive', __name__)

def build_drive_api_v3():
    credentials = google_auth.build_credentials()
    return googleapiclient.discovery.build('drive', 'v3', credentials=credentials).files()

def upload():
   if flask.request.method == 'POST':
    creds = google_auth.build_credentials()
    try: 
        build_drive_api_v3()
        file_metadata = {'name': 'download.jpeg'}
        media = MediaFileUpload('download.jpeg',
                                mimetype='image/jpeg')
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        print(F'File ID: {file.get("id")}')
    except HTTPerror as error:
        print(F'An error occurred: {error}')
        file = None
        
   return flask.render_template('upload.html')
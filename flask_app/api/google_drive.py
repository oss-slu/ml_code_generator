import tempfile

import flask
import googleapiclient.discovery
from apiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
from werkzeug.utils import secure_filename

from flask_app.api.google_auth import build_credentials

app = flask.Blueprint('google_drive', __name__)

def build_drive_api_v3():
   credentials = build_credentials()
   return googleapiclient.discovery.build('drive', 'v3', credentials=credentials).files()

def save_image(file_name, mime_type, file_data):
   drive_api = build_drive_api_v3()

   generate_ids_result = drive_api.generateIds(count=1).execute()
   file_id = generate_ids_result['ids'][0]

   body = {
      'id': file_id,
      'name': file_name,
      'mimeType': mime_type,
   }

   media_body = MediaIoBaseUpload(file_data,
                                   mimetype=mime_type,
                                   resumable=True)

   drive_api.create(body=body,
                     media_body=media_body,
                     fields='id,name,mimeType,createdTime,modifiedTime').execute()

   return file_id

def upload():
   if flask.request.method == 'POST':
      if 'file' not in flask.request.files:
            return flask.redirect(flask.request.url)

      file = flask.request.files['file']
      if (not file):
            return flask.redirect(flask.request.url)
            
      filename = secure_filename(file.filename)

      fp = tempfile.TemporaryFile()
      ch = file.read()
      fp.write(ch)
      fp.seek(0)

      mime_type = flask.request.headers['Content-Type']
      save_image(filename, mime_type, fp)

   return flask.render_template('upload.html')

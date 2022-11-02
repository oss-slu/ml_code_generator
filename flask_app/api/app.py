import functools
import json
import os

import flask

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import authentication
import google_drive

app = flask.Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

app.register_blueprint(authentication.app)
app.register_blueprint(google_drive.app)

@app.route('/')
def index():
    if authentication.is_logged_in():
        return flask.render_template('list.html', user_info=google_auth.get_user_info())

    return 'You are not currently logged in.'

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
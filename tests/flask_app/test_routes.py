import pytest
import io

from flask_app.flask_main import create_app

@pytest.fixture
def client():
   app = create_app()
   app.config["TESTING"] = True
   app.config["UPLOAD_FOLDER"] = 'tests/flask_app/test_data'
   with app.test_client() as client:
      yield client

def test_get_upload_page(client):
   response = client.get('/data')
   assert response.status_code == 200

def test_post_upload_page(client):
   data = {
      'file': (io.BytesIO(b"some random data"), "test_data.fake")
   }
   response = client.post('/data', data=data)
   assert response.status_code == 200

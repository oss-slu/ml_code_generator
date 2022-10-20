import io
import pytest

from flask_app.flask_main import create_app


@pytest.fixture(name="client")
def fixture_client():
   app = create_app()
   app.config["TESTING"] = True
   app.config["UPLOAD_FOLDER"] = 'tests/flask_app/test_data'
   with app.test_client() as flask_client:
      yield flask_client

def test_get_upload_page(client):
   response = client.get('/data')
   assert response.status_code == 200


def test_post_upload_page(client):
   data = {
      'file': (io.BytesIO(b"some random data"), "test_data.fake")
   }
   response = client.post('/data', data=data)
   assert response.status_code == 200

def test_download_get_method(client):
   response = client.get('/download')
   assert response.status_code == 200

def test_clean_get_method(client):
   csv = "tests/flask_app/test_data/fake_data.csv"
   #csv_data = open(csv, "rb")
   #data = {"file": (csv_data, "sample_data.csv")}
   with open(csv, "rb") as csv_data:
      data = {"file": (csv_data, "sample_data.csv")}
      response = client.post('/data', data=data)
      response = client.get('/clean')
      assert response.status_code == 200

def test_describe_get_method(client):
   csv = "tests/flask_app/test_data/fake_data.csv"
   with open(csv, "rb") as csv_data:
      data = {"file": (csv_data, "sample_data.csv")}
      response = client.post('/data', data=data)
      response = client.get('/describe')
      assert response.status_code == 200

def test_split_get_method(client):
   csv = "tests/flask_app/test_data/fake_data.csv"
   with open(csv, "rb") as csv_data:
      data = {"file": (csv_data, "sample_data.csv")}
      response = client.post('/data', data=data)
      response = client.get('/split')
      assert response.status_code == 200

def test_input_labels_get_method(client):
   csv = "tests/flask_app/test_data/fake_data.csv"
   with open(csv, "rb") as csv_data:
      data = {"file": (csv_data, "sample_data.csv")}
      response = client.post('/data', data=data)
      response = client.get('/input_labels')
      assert response.status_code == 200

#def test_input_labels_post_method(client):
#   csv = "tests/flask_app/test_data/fake_data.csv"
#   csv_data = open(csv, "rb")
#   data = {"file": (csv_data, "sample_data.csv")}
#   response = client.post('/data', data=data)
#   response = client.get('/input_labels')
#   response = client.post('/input_labels', data={'drop_label':'a'})
#   assert response.status_code == 200

def test_labels_get_method(client):
   csv = "tests/flask_app/test_data/fake_data.csv"
   with open(csv, "rb") as csv_data:
      data = {"file": (csv_data, "sample_data.csv")}
      response = client.post('/data', data=data)
      response = client.get('/labels')
      assert response.status_code == 200

#def test_labels_post_method(client):
#   csv = "tests/flask_app/test_data/fake_data.csv"
#   csv_data = open(csv, "rb")
#   data = {"file": (csv_data, "sample_data.csv")}
#   response = client.post('/data', data=data)
#   response = client.get('/labels')
#   response = client.post('/labels', data={'label':'a'})
#   assert response.status_code == 200

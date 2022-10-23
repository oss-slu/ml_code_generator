import io
from unittest import TestCase

from flask_app.flask_main import create_app


class TestRoutes(TestCase):
   def setUp(self):
      self.app = create_app()
      self.app.config["TESTING"] = True
      self.app.config["UPLOAD_FOLDER"] = 'tests/flask_app/test_data'
      self.client = self.app.test_client()

   def test_get_upload_page(self):
      print('upload')
      response = self.client.get('/data')
      assert response.status_code == 200

   def test_post_upload_page(self):
      data = {
         'file': (io.BytesIO(b"some random data"), "test_data.fake")
      }
      response = self.client.post('/data', data=data)
      assert response.status_code == 200

   def test_clean_get_method(self):
      csv = "tests/flask_app/test_data/fake_data.csv"
      #csv_data = open(csv, "rb")
      #data = {"file": (csv_data, "sample_data.csv")}
      with open(csv, "rb") as csv_data:
         data = {"file": (csv_data, "sample_data.csv")}
         response = self.client.post('/data', data=data)
         response = self.client.get('/clean')
         assert response.status_code == 200

   def test_download_get_method(self):
      response = self.client.get('/download')
      assert response.status_code == 200


   def test_describe_get_method(self):
      csv = "tests/flask_app/test_data/fake_data.csv"
      with open(csv, "rb") as csv_data:
         data = {"file": (csv_data, "sample_data.csv")}
         response = self.client.post('/data', data=data)
         response = self.client.get('/describe')
         assert response.status_code == 200

   def test_split_get_method(self):
      csv = "tests/flask_app/test_data/fake_data.csv"
      with open(csv, "rb") as csv_data:
         data = {"file": (csv_data, "sample_data.csv")}
         response = self.client.post('/data', data=data)
         response = self.client.get('/split')
         assert response.status_code == 200

   def test_input_labels_get_method(self):
      csv = "tests/flask_app/test_data/fake_data.csv"
      with open(csv, "rb") as csv_data:
         data = {"file": (csv_data, "sample_data.csv")}
         response = self.client.post('/data', data=data)
         response = self.client.get('/input_labels')
         assert response.status_code == 200

   def test_input_labels_post_method(self):
      csv = "tests/flask_app/test_data/fake_data.csv"
      with open(csv, "rb") as csv_data:
         data = {"file": (csv_data, "sample_data.csv")}
         response = self.client.post('/data', data=data)
         response = self.client.get('/input_labels')
         response = self.client.post('/input_labels', data={'drop_labels':'a'})
         assert response.status_code == 200

   def test_labels_get_method(self):
      csv = "tests/flask_app/test_data/fake_data.csv"
      with open(csv, "rb") as csv_data:
         data = {"file": (csv_data, "sample_data.csv")}
         response = self.client.post('/data', data=data)
         response = self.client.get('/labels')
         assert response.status_code == 200

   def test_labels_post_method(self):
      csv = "tests/flask_app/test_data/fake_data.csv"
      with open(csv, "rb") as csv_data:
         data = {"file": (csv_data, "sample_data.csv")}
         self.client.get('/download')
         response = self.client.post('/data', data=data)
         response = self.client.get('/labels')
         response = self.client.post('/labels', data={'label':'a'})
         # 302 is a successful redirect code
         # /labels redirects to /input_labels
         assert (response.status_code in [200, 302])

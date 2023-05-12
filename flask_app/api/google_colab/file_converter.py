import json
import tempfile
import re
from flask_app.api.generator import generator

def make_ipynb():
   code = generator.download_code()
   print(code)

   ##################################################################
   # Thanks ChatGPT, for this bit of wisdom about regular expressions
   ##################################################################
   # Define the new file path you want to use
   new_file_path = '/content/drive/My Drive/'
   # Define a regular expression pattern that matches the file path and any characters before it
   pattern = r'^(.*pd\.read_csv\(").*/([^/]+\.[^/]+)(?="\))'
   # Use the regular expression to replace the file path in the original string
   code = re.sub(pattern, r'\g<1>' + new_file_path + r'\2', code, flags=re.MULTILINE)

   template = {
      "cells": [
         {
         "cell_type": "code",
         "metadata": {},
         "outputs": [],
         "source": [
           "from google.colab import drive\n",
           "drive.mount('/content/drive')"
         ],
         },
         {
            "cell_type": "code",
            "metadata": {},
            "outputs": [],
            "source": [
               code
            ]
         }
      ],
      "metadata": {
         "language_info": {
            "name": "python"
         },
         "orig_nbformat": 4
      },
      "nbformat": 4,
      "nbformat_minor": 2
   }

   with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
      json.dump(template, tmp)
      tmp.flush()
      return tmp.name

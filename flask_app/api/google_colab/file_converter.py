import json
from datetime import date
import os.path
from flask_app.api.generator import generator

def make_ipynb():
   code = generator.download_code()
   file_name = "data/"+ str(date.today()) + ".ipynb"
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
   if os.path.exists(file_name):
      with open (file_name, mode = "w",encoding="utf-8") as outfile:
         json.dump(template,outfile)
   else:
      with open (file_name, mode = "x",encoding="utf-8") as outfile:
         json.dump(template,outfile)

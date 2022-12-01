import json

from flask_app.api.generator import generator

def make_ipynb():
   code = code = generator.download_code()
   template = {"cells":[{"cell_type":"code","metadata":{},"outputs":[],"source":[code]}],
   "metadata":{"language_info":{"name":"python"},"orig_nbformat":4},"nbformat":4,"nbformat_minor":2}
   with open ("data/sample.ipynb", mode = "w",encoding="utf-8") as outfile:
      json.dump(template,outfile)








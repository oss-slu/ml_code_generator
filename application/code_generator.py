import pandas as pd
from model import code_blocks
from application.parse_template import parse_template
from application.code_templates import read_csv
from application.code_templates import describe_data

class CodeGenerator:
   def __init__(self, template_mapping):
      self.blocks = code_blocks.AllBlocks()
      self.function_mapping = template_mapping
      self.data = {}


   def load_data(self, csv_file):
      self._save('dataframe', self._parse_and_execute('read_csv', [csv_file]))
      return self.data['dataframe'].shape

   def describe_data(self):
      output = self._parse_and_execute('describe_data', ['dataframe'])
      return output

   def clean_data(self):
      self._parse_and_execute('clean_data', ['dataframe'])
      return self.data['dataframe'].shape

   def get_labels(self):
      keys = self._parse_and_execute('get_keys', ['dataframe'])
      return keys

   def download_code(self):
      return self.blocks.to_text()

   def _create_new_block(self, comment, statements):
      block = code_blocks.CodeBlock(comment, statements)
      self.blocks.add_next_block(block)

   def _parse_and_execute(self, template, args):
      replaced_args = []
      string_args = []
      for arg in args:
         if arg in self.data:
            replaced_args.append(self.data[arg])
            string_args.append(arg)
         else:
            replaced_args.append(arg)
            string_args.append('\"'+arg+'\"')

      (comments, code) = parse_template('application/code_templates/'+template+'.py', string_args)
      self._create_new_block(comments[0], code)
      output = self.function_mapping[template](replaced_args)
      return output

   def _save(self, key, value):
      self.data[key] = value

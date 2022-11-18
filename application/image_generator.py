import os
from model import code_blocks
from pandas_code.mapping import template_mapping
from pandas_code.parse_template import parse_template

class ImageGenerator:
   def __init__(self, template_mapping, parse_template):
      self.blocks = code_blocks.AllBlocks()
      self.function_mapping = template_mapping
      self.parse_template = parse_template
      self.data = {}
      
   def load_images(self, images_directory):
      #Dividing the data in different batches and showing labels
      self.data = self._parse_and_execute('load_images', [images_directory]) 
      return self.data
   
   def validate_images(self, images_directory):
      olamba = self._parse_and_execute('validate_images', [images_directory])
      return 
   
   def preprocess_images(self, images_directory): #directory after validating the images
      normalized_data = self._parse_and_execute('preprocess_images', [images_directory])
      return 
   
   def split_images(self, train_ratio, val_ratio, test_ratio ):
      (train, val, test) = self._parse_and_execute('split_images', [train_ratio, val_ratio, test_ratio])
      return 
   
   def train_model(self, data, train, val, epochs):
      self._parse_and_execute('images_mode', [data, train, val, epochs])
      return

   def download_code(self):
      return self.blocks.to_text()

   def _parse_and_execute(self, template, args):
      replaced_args = []
      string_args = []
      for arg in args:
         if isinstance(arg, str) and arg in self.data:
            replaced_args.append(self.data[arg])
            string_args.append(arg)
         else:
            replaced_args.append(arg)
            if isinstance(arg, str):
               string_args.append('\"'+arg+'\"')
            else:
               string_args.append(str(arg))

      (comments, code) = self.parse_template(template, string_args)
      self._create_new_block(comments[0], code)
      output = self.function_mapping[template](replaced_args)  # where the code is executed
      return output
   
   def _create_new_block(self, comment, statements):
      block = code_blocks.CodeBlock(comment, statements)
      self.blocks.add_next_block(block)
             
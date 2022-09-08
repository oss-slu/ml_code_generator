from model import code_blocks
class CodeGenerator:
   def __init__(self, template_mapping, parse_template):
      self.blocks = code_blocks.AllBlocks()
      self.function_mapping = template_mapping
      self.parse_template = parse_template
      self.data = {}

   def get_data(self):
      return self.data['dataframe']

   def load_data(self, csv_file):
      dataframe = self._parse_and_execute('read_csv', [csv_file])
      self._save('dataframe', dataframe)
      self._save('X', dataframe)
      return self.data['dataframe'].shape

   def describe_data(self):
      output = self._parse_and_execute('describe_data', ['dataframe'])
      return output

   def clean_data(self):
      self._parse_and_execute('clean_data', ['dataframe'])
      return self.data['dataframe'].shape

   def get_labels(self):
      keys = self._parse_and_execute('get_keys', ['X'])
      return keys.values.tolist()

   def drop_x(self, input_labels):
      x_values = self._parse_and_execute('drop_x', ['X', input_labels])
      self._save('X', x_values)

   def select_y(self, output_label):
      x_values, y_values = self._parse_and_execute('select_y', ['X', output_label])
      self._save('X', x_values)
      self._save('Y', y_values)

   def split_data(self, train_ratio = 0.8, seed = 200):
      (train, test) = self._parse_and_execute('split',['X',train_ratio,seed])
      self.data['train'] = train
      self.data['test'] = test
      return self.data['train'].shape

   def download_code(self):
      return self.blocks.to_text()

   def _create_new_block(self, comment, statements):
      block = code_blocks.CodeBlock(comment, statements)
      self.blocks.add_next_block(block)

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
      output = self.function_mapping[template](replaced_args)
      return output

   def _save(self, key, value):
      self.data[key] = value

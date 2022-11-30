from application.code_parser import CodeParser
from model import code_blocks
class CodeGenerator(CodeParser):
   def __init__(self, template_mapping, parse_template):
      super(). __init__(template_mapping, parse_template)

   def get_data(self):
      return self.data['dataframe']

   def load_data(self, csv_file):
      dataframe = self._parse_and_execute('read_csv', [csv_file])
      self._save('dataframe', dataframe)
      self._save('x_values', dataframe)
      return self.data['dataframe'].shape

   def describe_data(self):
      output = self._parse_and_execute('describe_data', ['dataframe'])
      return output

   def clean_data(self):
      self._parse_and_execute('clean_data', ['dataframe'])
      return self.data['dataframe'].shape

   def get_labels(self):
      keys = self._parse_and_execute('get_keys', ['dataframe'])
      return keys.values.tolist()

   def select_y(self, output_label):
      x_values, y_values = self._parse_and_execute('select_y', ['dataframe', output_label])
      self._save('x_values', x_values)
      self._save('y_values', y_values)

   def drop_x(self, input_labels):
      x_values = self._parse_and_execute('drop_x', ['x_values', input_labels])
      self._save('x_values', x_values)

   def split_data(self, train_ratio = 0.8, seed = 200):
      # the ordering of x/y train/test is different here but I don't know why
      (x_train, y_train, x_test, y_test)=self._parse_and_execute(
         'split',['x_values','y_values',1-train_ratio,seed]
      )
      self._save('x_train', x_train)
      self._save('x_test', x_test)
      self._save('y_train', y_train)
      self._save('y_test', y_test)
      return self.data['x_train'].shape

   def train_model(self):
      model = self._parse_and_execute('train_model', ['x_train', 'y_train'])
      return model

   def download_code(self):
      return self.blocks.to_text()

   def _create_new_block(self, comment, statements):
      block = code_blocks.CodeBlock(comment, statements)
      self.blocks.add_next_block(block)

   def _parse_and_execute(self, template, args):
      print("Args is ", args)
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

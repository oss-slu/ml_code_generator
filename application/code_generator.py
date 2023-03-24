from model import code_blocks
from pandas_code.code_templates import is_categorical

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
      return self.data['dataframe'].shape

   def describe_data(self):
      output = self._parse_and_execute('describe_data', ['dataframe'])
      return output

   def get_labels(self):
      keys = self._parse_and_execute('get_keys', ['dataframe'])
      return keys.values.tolist()

   def drop_x(self, input_labels):
      dataframe = self._parse_and_execute('drop_x', ['dataframe', input_labels])
      self._save('dataframe', dataframe)

   def clean_data(self):
      dataframe = self._parse_and_execute('clean_data', ['dataframe'])
      self._save('dataframe', dataframe)
      return self.data['dataframe'].shape

   def select_y(self, output_label):
      x_values, y_values = self._parse_and_execute('select_y', ['dataframe', output_label])
      self._save('x_values', x_values)
      self._save('y_values', y_values)

   def one_hot_encode_x_data(self):
      x_values = self.data["x_values"]
      y_values = self.data["y_values"]
      create_code = is_categorical.is_categorical(x_values, y_values)
      if create_code[0]:
         x_values = self._parse_and_execute('one_hot_encode_x_data', ['x_values'])
      if create_code[1]:
         print("trying to encode y data")
         y_values = self._parse_and_execute('one_hot_encode_y_data', ['y_values'])
         print("encoded y values")
      self._save('x_values', x_values)
      self._save('y_values', y_values)

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

   def train_lin_reg(self):
      model = self._parse_and_execute('train_lin_reg', ['x_train', 'y_train'])
      self._save('model', model)
      return model

   def predict_lin_reg(self):
      (train_preds, test_preds) = self._parse_and_execute(
         'predict_lin_reg', ['model', 'x_train', 'x_test']
      )
      self._save('train_preds', train_preds)
      self._save('test_preds', test_preds)

   def eval_lin_reg(self):
      error_change = self._parse_and_execute(
         'eval_lin_reg', ['y_train', 'y_test', 'train_preds', 'test_preds']
      )
      self._save('error_change', error_change)

   def train_decision_tree(self):
      model = self._parse_and_execute('train_decision_tree', ['x_train', 'y_train'])
      self._save('model', model)      # will need to be renamed if using multiple models
      return model

   def predict_decision_tree(self):
      test_preds = self._parse_and_execute('predict_decision_tree', ['model', 'x_test'])
      self._save('test_preds', test_preds)

   def eval_decision_tree(self):
      self._parse_and_execute('eval_decision_tree', ['y_test', 'test_preds'])
      # ^ this is going to the predict function again

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
      output = self.function_mapping[template](replaced_args)  # where the code is executed
      return output

   def _save(self, key, value):
      self.data[key] = value

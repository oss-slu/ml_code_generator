from application.code_parser import CodeParser
class CodeGenerator(CodeParser):
   def get_data(self):
      return self.data['dataframe']

   def load_data(self, csv_file):
      dataframe = self.parse_and_execute('read_csv', [csv_file])
      self.save('dataframe', dataframe)
      return self.data['dataframe'].shape

   def describe_data(self):
      output = self.parse_and_execute('describe_data', ['dataframe'])
      return output

   def get_labels(self):
      keys = self.parse_and_execute('get_keys', ['dataframe'])
      return keys.values.tolist()

   def select_y(self, output_label):
      x_values, y_values = self.parse_and_execute('select_y', ['dataframe', output_label])
      self.save('x_values', x_values)
      self.save('y_values', y_values)

   def drop_x(self, input_labels):
      dataframe = self.parse_and_execute('drop_x', ['dataframe', input_labels])
      self.save('dataframe', dataframe)

   def clean_data(self):
      dataframe = self.parse_and_execute('clean_data', ['dataframe'])
      self.save('dataframe', dataframe)
      return self.data['dataframe'].shape

   def split_data(self, train_ratio = 0.8, seed = 200):
      # the ordering of x/y train/test is different here but I don't know why
      (x_train, y_train, x_test, y_test)=self.parse_and_execute(
         'split',['x_values','y_values',1-train_ratio,seed]
      )
      self.save('x_train', x_train)
      self.save('x_test', x_test)
      self.save('y_train', y_train)
      self.save('y_test', y_test)
      return self.data['x_train'].shape

   def train_lin_reg(self):
      model = self.parse_and_execute('train_lin_reg', ['x_train', 'y_train'])
      self.save('model', model)
      return model

   def lin_reg_predict(self):
      (train_preds, test_preds) = self.parse_and_execute(
         'lin_reg_predict', ['model', 'x_train', 'x_test']
      )
      self.save('train_preds', train_preds)
      self.save('test_preds', test_preds)

   def eval_lin_reg(self):
      error_change = self.parse_and_execute(
         'eval_lin_reg', ['y_train', 'y_test', 'train_preds', 'test_preds']
      )
      self.save('error_change', error_change)

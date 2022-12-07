from pandas_code.parse_template import get_args_index
from pandas_code.parse_template import replace_args_with_values
from pandas_code.parse_template import parse_template

# tests for parsing out the argument index
def test_args_0():
   args_string='args[0]'
   args_index = get_args_index(args_string)
   assert args_index == 0

def test_args_9():
   args_string='args[9]'
   args_index = get_args_index(args_string)
   assert args_index == 9

def test_args_10():
   args_string='args[10]'
   args_index = get_args_index(args_string)
   assert args_index == 10

def test_args_99999():
   args_string='args[99999]'
   args_index = get_args_index(args_string)
   assert args_index == 99999

# tests for replacing args[num] literal with an args value

def test_one_args_per_line():
   line = 'print(args[0])'
   args=["'kate'"]
   line_replaced = replace_args_with_values(line, args)
   assert line_replaced=='print(\'kate\')'

def test_one_args_with_special_chars():
   line = 'print(args[0])'
   args=["\'~/Downloads/possum.csv\'"]
   line_replaced = replace_args_with_values(line, args)
   print(line_replaced)
   assert line_replaced=='print(\'~/Downloads/possum.csv\')'

def test_two_args_per_line():
   line = 'print(args[0],args[1])'
   args=["'kate'", '5']
   line_replaced = replace_args_with_values(line, args)
   assert line_replaced=='print(\'kate\',5)'

def test_three_args_per_line():
   line = 'print(args[0],args[1],args[2])'
   args=["'kate'", '5', "'data'"]
   line_replaced = replace_args_with_values(line, args)
   assert line_replaced=='print(\'kate\',5,\'data\')'

def test_parse_train():
   template_name = 'train_model'
   args = ['x_values', 'y_values']
   parse_template(template_name, args)

def test_parse_split():
   template_name = 'split'
   args = ['X', 'Y', '0.8', '200']
   parse_template(template_name, args)

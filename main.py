import sys
from application import code_generator
from pandas_code.mapping import template_mapping
from pandas_code.parse_template import parse_template

def run_generator(args):
   print(args)
   input_file = args[1]
   generator = code_generator.CodeGenerator(template_mapping, parse_template)
   generator.load_data(input_file)
   data_summary = generator.describe_data()
   print(data_summary.to_csv())
   print(generator.get_labels())     # feature names
   generator.drop_x(['eye'])
   clean_data = generator.clean_data()
   print(clean_data)
   generator.select_y("Pop") # the y can't be continuous for decision trees
   generator.one_hot_encode_x_data()
   print("\n left one hot \n")
   print(generator.split_data())
   generator.train_decision_tree()
   generator.predict_decision_tree()
   generator.eval_decision_tree()
   code = generator.download_code()
   print(code)
#process the arguments
if __name__ == '__main__':
   run_generator(sys.argv)

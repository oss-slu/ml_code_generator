import sys
from application import code_generator
from pandas_code.mapping import template_mapping
from pandas_code.parse_template import parse_template

#process the arguments
print(sys.argv)
input_file = sys.argv[1]
generator = code_generator.CodeGenerator(template_mapping, parse_template)
generator.load_data(input_file)
data_summary = generator.describe_data()
print(data_summary.to_csv())
clean_data = generator.clean_data()
print(clean_data)
print(generator.get_labels())
print(generator.split_data())
code = generator.download_code()
print(code)

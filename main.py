import sys
from application import code_generator

print(sys.argv)
input_file = sys.argv[1]
generator = code_generator.CodeGenerator()
generator.load_data(input_file)
data_summary = generator.describe_data()
print(data_summary.to_csv())
print(generator.get_labels())
code = generator.download_code()
print(code)

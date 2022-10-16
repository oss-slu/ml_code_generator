from application import code_generator
from pandas_code.mapping import template_mapping
from pandas_code.parse_template import parse_template


generator = code_generator.CodeGenerator(template_mapping, parse_template)

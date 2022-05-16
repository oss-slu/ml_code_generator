from application import code_generator
from pandas_code.mapping import template_mapping
from pandas_code.parse_template import parse_template


def test_select_y():
   generator = code_generator.CodeGenerator(template_mapping, parse_template)
   generator.load_data('tests/data/sample_data.csv')
   generator.select_y('a')

def test_drop_x():
   generator = code_generator.CodeGenerator(template_mapping, parse_template)
   generator.load_data('tests/data/sample_data.csv')
   generator.drop_x(['a'])

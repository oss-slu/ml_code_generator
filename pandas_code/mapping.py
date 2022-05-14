from pandas_code.code_templates import read_csv
from pandas_code.code_templates import describe_data
from pandas_code.code_templates import clean_data
from pandas_code.code_templates import get_keys
from pandas_code.code_templates import split
from pandas_code.code_templates import select_y

template_mapping = {
   'read_csv':read_csv.get_code,
   'describe_data':describe_data.get_code,
   'clean_data':clean_data.get_code,
   'get_keys':get_keys.get_code,
   'split':split.get_code,
   'select_y':select_y.get_code
}

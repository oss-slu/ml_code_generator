from application.code_templates import read_csv
from application.code_templates import describe_data
from application.code_templates import clean_data
from application.code_templates import get_keys

template_mapping = {
   'read_csv':read_csv.get_code,
   'describe_data':describe_data.get_code,
   'clean_data':clean_data.get_code,
   'get_keys':get_keys.get_code
}

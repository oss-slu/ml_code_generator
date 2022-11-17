from pandas_code.code_templates import read_csv
from pandas_code.code_templates import describe_data
from pandas_code.code_templates import clean_data
from pandas_code.code_templates import get_keys
from pandas_code.code_templates import split
from pandas_code.code_templates import select_y
from pandas_code.code_templates import drop_x
from pandas_code.code_templates import train_lin_reg
from pandas_code.code_templates import lin_reg_predict
from pandas_code.code_templates import eval_lin_reg

template_mapping = {
   'read_csv': read_csv.get_code,
   'describe_data': describe_data.get_code,
   'clean_data': clean_data.get_code,
   'get_keys': get_keys.get_code,
   'split': split.get_code,
   'select_y': select_y.get_code,
   'drop_x': drop_x.get_code,
   'train_lin_reg': train_lin_reg.get_code,
   'lin_reg_predict': lin_reg_predict.get_code,
   'eval_lin_reg': eval_lin_reg.get_code
}

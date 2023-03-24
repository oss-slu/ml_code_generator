from pandas_code.code_templates import clean_data
from pandas_code.code_templates import describe_data
from pandas_code.code_templates import drop_x
from pandas_code.code_templates import eval_decision_tree
from pandas_code.code_templates import eval_lin_reg
from pandas_code.code_templates import get_keys
from pandas_code.code_templates import one_hot_encode_x_data
from pandas_code.code_templates import one_hot_encode_y_data
from pandas_code.code_templates import predict_decision_tree
from pandas_code.code_templates import predict_lin_reg
from pandas_code.code_templates import read_csv
from pandas_code.code_templates import select_y
from pandas_code.code_templates import split
from pandas_code.code_templates import train_decision_tree
from pandas_code.code_templates import train_lin_reg

template_mapping = {
   'clean_data':clean_data.get_code,
   'describe_data':describe_data.get_code,
   'drop_x':drop_x.get_code,
   'eval_decision_tree':eval_decision_tree.get_code,
   'eval_lin_reg': eval_lin_reg.get_code,
   'get_keys':get_keys.get_code,
   'one_hot_encode_x_data':one_hot_encode_x_data.get_code,
   'one_hot_encode_y_data':one_hot_encode_y_data.get_code,
   'predict_decision_tree':predict_decision_tree.get_code,
   'predict_lin_reg':predict_lin_reg.get_code,
   'read_csv':read_csv.get_code,
   'select_y':select_y.get_code,
   'split':split.get_code,
   'train_decision_tree':train_decision_tree.get_code,
   'train_lin_reg':train_lin_reg.get_code
}

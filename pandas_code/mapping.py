from pandas_code.code_templates import read_csv
from pandas_code.code_templates import describe_data
from pandas_code.code_templates import clean_data
from pandas_code.code_templates import get_keys
from pandas_code.code_templates import split
from pandas_code.code_templates import select_y
from pandas_code.code_templates import drop_x
from pandas_code.code_templates import train_model
from pandas_code.code_templates import load_images
from pandas_code.code_templates import validate_images
from pandas_code.code_templates import preprocess_images
from pandas_code.code_templates import split_images
from pandas_code.code_templates import images_model
from pandas_code.code_templates import visualize
template_mapping = {
   'read_csv':read_csv.get_code,
   'describe_data':describe_data.get_code,
   'clean_data':clean_data.get_code,
   'get_keys':get_keys.get_code,
   'split':split.get_code,
   'select_y':select_y.get_code,
   'drop_x':drop_x.get_code,
   'train_model':train_model.get_code,
   'load_images':load_images.get_code,
   'validate_images':validate_images.get_code,
   'preprocess_images':preprocess_images.get_code,
   'split_images':split_images.get_code,
   'images_model':images_model.get_code,
   'visualize':visualize.get_code
}

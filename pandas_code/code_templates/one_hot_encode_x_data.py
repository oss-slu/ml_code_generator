# apply one hot encoding to any categorical variables
# maybe change so that is before choosing y so it can all get one hot encoded if needed
#from pandas_code.code_templates import is_categorical

from pandas.api.types import is_numeric_dtype
import pandas as pd
def get_code(args):
   cols = list(args[0])
   print(is_numeric_dtype(args[0][cols[0]]))
   for i in cols:
      if not is_numeric_dtype(args[0][i]): #test comment
         one_hot = pd.get_dummies(args[0][i])
         args[0] = args[0].drop(i, axis = 1)
         args[0] = args[0].join(one_hot)
   return args[0]

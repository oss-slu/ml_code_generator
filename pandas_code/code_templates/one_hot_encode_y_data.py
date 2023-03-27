# apply one hot encoding to any categorical variables in y data
import pandas as pd
def get_code(args):
   one_hot = pd.get_dummies(args[0])
   args[0] = one_hot
   return args[0]

# apply one hot encoding to any categorical variables
import pandas as pd
def get_code(args):
   one_hot = pd.get_dummies(args[0])
   #args[0] = args[0].drop(i, axis = 1)
   args[0] = one_hot
   print("y encoded data", args[0])
   return args[0]

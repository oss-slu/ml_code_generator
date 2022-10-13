# Train a linear regression model
from sklearn.linear_model import LinearRegression
import pandas as pd
from numpy import ndim

def get_code(args):
   print("args[0] ", args[0])
   #args[0] = [args[0]]
   #args[0] = np.reshape(81, 0)
   #args[1] = np.reshape(-1, 1)
   print("The X's\n IS THIS A DATA FRAME????\n ",  isinstance(args[0], pd.DataFrame))
   print("???? \n WHAT ARE X'S DIMENSIONS", args[0].ndim)
   print("???? \n WHAT ARE Y'S DIMENSIONS", args[1].ndim)
   model = LinearRegression().fit(args[0], args[1])
   return model
   # assuming that the args passed in are training features and training labels


# split the data set into training and test data
import pandas as pd

def get_code(args):

   y_values = args[0][args[1]]

   print("Pre-Selecting Y\n IS THIS A DATA FRAME????\n ",  isinstance(args[0], pd.DataFrame))
   x_values = args[0].drop(args[1], axis = 1)
   # y_values = args[0][args[1]]  # returns a list and not a dataframe
   #y_values = args[0].loc(:, [[args[1]]) # says the ':' is invalid
   print("Selecting Y\n IS THIS A DATA FRAME????\n ",  isinstance(y_values, pd.DataFrame))
   print('X Values: \n', x_values)
   print('Y Values: \n', y_values)
   return (x_values, y_values)

# split the data set into training and test data
import pandas as pd

def get_code(args):
   y_values = args[0][args[1]]
   x_values = args[0].drop(args[1], axis = 1)
   return (x_values, y_values)

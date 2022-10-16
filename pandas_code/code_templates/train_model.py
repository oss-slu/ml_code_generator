# Train a linear regression model
from sklearn.linear_model import LinearRegression
import pandas as pd

def get_code(args):
   model = LinearRegression().fit(args[0], args[1])
   return model
   # assuming that the args passed in are training features and training labels

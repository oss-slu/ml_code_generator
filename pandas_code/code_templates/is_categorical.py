from pandas.api.types import is_numeric_dtype
import pandas as pd

def is_categorical(x_data, y_data):
   print("\n", "hit dtype")
   y_is_cat = False
   x_is_cat = False
   for col in x_data:
      print(is_numeric_dtype(x_data[col]), "x type is ", x_data[col].dtype)
      if not is_numeric_dtype(x_data[col]):
         x_is_cat = True

   print(is_numeric_dtype(y_data), "y type is ", y_data.dtype)
   if not is_numeric_dtype(y_data):
      y_is_cat = True   
   return (x_is_cat, y_is_cat)

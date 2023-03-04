from pandas.api.types import is_numeric_dtype
import pandas as pd

def is_categorical(data):
   print("\n", "hit dtype")
   for col in data:
      print(is_numeric_dtype(data[col]), "type is ", data[col].dtype )
      if not is_numeric_dtype(data[col]):
         return True
   return False

from pandas.api.types import is_numeric_dtype

def is_categorical(x_data, y_data):
   y_is_cat = False
   x_is_cat = False
   for col in x_data:
      if not is_numeric_dtype(x_data[col]):
         x_is_cat = True
   if not is_numeric_dtype(y_data):
      y_is_cat = True   
   return (x_is_cat, y_is_cat)
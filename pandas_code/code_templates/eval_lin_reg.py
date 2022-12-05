# evaluate the effectiveness of the model
from sklearn.metrics import mean_squared_error
def get_code(args):
   train_error = mean_squared_error(args[0], args[2])
   test_error = mean_squared_error(args[1], args[3])
   error_change = abs(test_error - train_error)
   return error_change
   # ^ don't really need to return but pylint complained

# evaluate the effectiveness of the model
from sklearn.metrics import mean_squared_error
def get_code(args):
   train_error = mean_squared_error(args[0], args[2])
   test_error = mean_squared_error(args[1], args[3])
   error_change = abs(test_error - train_error)
   print("Mean Squared error on train set =", train_error)
   print("Mean Squared error on test set =", test_error)
   print("Difference between test error and train error =", error_change)
   return error_change

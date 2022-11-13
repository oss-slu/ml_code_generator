from sklearn.model_selection import train_test_split
import numpy as np
# split the data set into training and test data
def get_code(args):
   x_train, x_test, y_train, y_test = train_test_split(args[0], args[1],
      test_size = args[2], random_state = args[3])
   y_train = np.asarray(y_train)
   y_test = np.asarray(y_test)
   return (x_train, y_train, x_test, y_test)

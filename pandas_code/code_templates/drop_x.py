# split the data set into training and test data
def get_code(args):
   x_values = args[0].drop(args[1], axis=1)
   return x_values
   
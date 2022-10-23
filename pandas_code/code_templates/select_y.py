# split the data set into training and test data
def get_code(args):
   Y = args[0][args[1]]
   X = args[0].drop(args[1], axis = 1)
   return (X, Y)

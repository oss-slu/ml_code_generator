# split the data set into training and test data
def get_code(args):
   X = args[0].drop(args[1], axis=1)
   Y = args[0][args[1]]
   return (X, Y)

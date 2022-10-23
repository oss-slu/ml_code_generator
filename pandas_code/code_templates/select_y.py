# split the data set into training and test data
def get_code(args):
   y = args[0][args[1]]
   x = args[0].drop(args[1], axis = 1)
   return (x, y)

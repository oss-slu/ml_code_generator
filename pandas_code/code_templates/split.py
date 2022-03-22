# split the data set into training and test data
def get_code(args):
   train = args[0].sample(frac=args[1], random_state=args[2])
   test = args[0].drop(train.index)
   return (train, test)

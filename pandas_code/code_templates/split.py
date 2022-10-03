from sklearn.model_selection import train_test_split

# split the data set into training and test data
def get_code(args):
   X = args[3]
   y = args[4]
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 - args[1], random_state=args[2])
   #train = args[0].sample(frac=args[1], random_state=args[2])
   #test = args[0].drop(train.index)
   print( "training data:", train)
   return (train, test)

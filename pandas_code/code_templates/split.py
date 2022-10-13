from sklearn.model_selection import train_test_split
import pandas as pd

# split the data set into training and test data
def get_code(args):
   print("\n features: \n", args[0])
   print("\n labels: \n", args[1])
   x_train,x_test,y_train,y_test=train_test_split(args[0],args[1],test_size=1-args[2],random_state=args[3])
   #train = args[0].sample(frac=args[1], random_state=args[2])
   #test = args[0].drop(train.index)
   print("The train X's\n IS THIS A DATA FRAME????\n ",  isinstance(x_train, pd.DataFrame))
   print("The train Y's\n IS THIS A DATA FRAME????\n ",  isinstance(y_train, pd.DataFrame))
   return (x_train, y_train, x_test, y_test)

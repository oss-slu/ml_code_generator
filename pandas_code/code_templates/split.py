from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# split the data set into training and test data
def get_code(args):
   obj_col = [ind for ind, key in enumerate(args[0].keys()) if args[0][key].dtypes == 'object']
   LE=LabelEncoder()
   args[1] = LE.fit_transform(args[1]) if args[1].dtypes == 'object' else args[1]
   CT =  ColumnTransformer([('encoder', OneHotEncoder(), obj_col)], remainder='passthrough')
   args[0] = np.array(CT.fit_transform(args[0])) if  len(obj_col) > 0 else args[0]  
   x_train, x_test, y_train, y_test = train_test_split(args[0], args[1], test_size = args[2], random_state = args[3])
   y_train = np.asarray(y_train)
   y_test = np.asarray(y_test)
   return (x_train, y_train, x_test, y_test)

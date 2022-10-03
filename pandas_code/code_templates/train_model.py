# Train a linear regression model
from sklearn.linear_model import LinearRegression
import numpy as np

def get_code(args):
    print("args[0] ", args[0])
    args[0] = [args[0]]
    #args[0] = np.reshape(81, 0)
    #args[1] = np.reshape(-1, 1)
    model = LinearRegression().fit(args[0], args[1])
    
    return model
    # assuming that the args passed in are training features and training labels
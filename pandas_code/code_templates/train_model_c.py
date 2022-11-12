# Train a Decision Tree model
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

def get_code(args):
   model = DecisionTreeClassifier().fit(args[0], args[1])
   y_pred = model.predict(args[2])
   print("Accuracy: {}%".format(round(metrics.accuracy_score(args[3], y_pred)*100,2)))
   return model
   # assuming that the args passed in are training features and training labels

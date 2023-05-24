# Train a decision tree model
from sklearn.tree import DecisionTreeClassifier
def get_code(args):
   model = DecisionTreeClassifier().fit(args[0], args[1])
   return model

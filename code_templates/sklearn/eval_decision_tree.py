# evaluate the effectiveness of the model
from sklearn.metrics import classification_report
def get_code(args):
   print(classification_report(args[0], args[1]))

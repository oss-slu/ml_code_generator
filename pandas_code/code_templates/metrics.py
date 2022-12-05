from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
#Finding the accuracy of the model
def get_code(args):
   pre = Precision()
   re = Recall()
   acc = BinaryAccuracy()
   # test = args[0].map(lambda x, y: (x/255, y))
   for batch in args[0].as_numpy_iterator():
      X, y = batch
      yhat = args[1].predict(X)
      pre.update_state(y, yhat)
      re.update_state(y, yhat)
      acc.update_state(y, yhat)
   print(f'Precision: {pre.result().numpy()}, \
   Recall: {re.result().numpy()}, Accuracy: {acc.result().numpy()}')
   return pre, re, acc

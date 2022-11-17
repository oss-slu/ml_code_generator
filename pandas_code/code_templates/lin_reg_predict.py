# get model predictions for the train and test set
def get_code(args):
   test_preds = args[0].predict(args[1])
   train_preds = args[0].predict(args[2])
   return (test_preds, train_preds)

   # need to take in model x_train x_test
   # return test_preds train_preds

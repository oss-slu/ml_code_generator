# get model predictions for the train and test set
def get_code(args):
   test_preds = args[0].predict(args[1])
   return test_preds
   
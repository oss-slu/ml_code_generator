# get model predictions for the train and test set
def get_code(args):
   train_preds = args[0].predict(args[1])
   test_preds = args[0].predict(args[2])
   return (train_preds, test_preds)

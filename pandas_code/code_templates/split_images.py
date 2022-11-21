#splitting images
def get_code(args):
   train_size = int(len(args[0]) * args[1])
   val_size = int(len(args[0]) * args[2]) + 1
   test_size = int(len(args[0])* args[3]) + 1
   train = args[0].take(train_size)
   val = args[0].skip(train_size).take(val_size)
   test = args[0].skip(train_size + val_size).take(test_size)
   return train, val, test

# def split_images(self, train_ration, val_ratio, test_ratio):
#    # Splitting images
#    train_size = int(len(data) * 0.7)
#    val_size = int(len(data) * .2) + 1
#    test_size = int(len(data)* .1) + 1

#    train = data.take((train_size))
#    val = data.skip(train_size).take(val_size)
#    test = data.skip(train_size + val_size).take(test_size)

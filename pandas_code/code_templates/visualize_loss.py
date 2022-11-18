import matplotlib.pyplot as plt
#visulize loss
def get_code(args):
   acc = args[0].history['loss']
   val_acc = args[0].history['val_loss']
   
   plt.figure(figsize=(8, 8))
   plt.subplot(1, 2, 1)
   plt.plot(acc, label='Training Accuracy')
   plt.plot(val_acc, label='Validation Accuracy')
   plt.legend(loc='lower right')
   plt.title('Training and Validation Accuracy')
   plt.show()
   
   # def visualize(self):
   #    acc = history.history['accuracy']
   #    val_acc = history.history['val_accuracy']

   #    loss = history.history['loss']
   #    val_loss = history.history['val_loss']

   #    epochs_range = range(epochs)

   #    plt.figure(figsize=(8, 8))
   #    plt.subplot(1, 2, 1)
   #    plt.plot(epochs_range, acc, label='Training Accuracy')
   #    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
   #    plt.legend(loc='lower right')
   #    plt.title('Training and Validation Accuracy')

   #    plt.subplot(1, 2, 2)
   #    plt.plot(epochs_range, loss, label='Training Loss')
   #    plt.plot(epochs_range, val_loss, label='Validation Loss')
   #    plt.legend(loc='upper right')
   #    plt.title('Training and Validation Loss')
   #    plt.show()
   
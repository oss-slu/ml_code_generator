import matplotlib.pyplot as plt
#visualize loss
def get_code(args):
   acc = args[0].history['accuracy']
   val_acc = args[0].history['val_accuracy']

   plt.figure(figsize=(8, 8))
   plt.subplot(1, 2, 1)
   plt.plot(acc, label='Training Accuracy')
   plt.plot(val_acc, label='Validation Accuracy')
   plt.legend(loc='lower right')
   plt.title('Training and Validation Accuracy')
   plt.show()

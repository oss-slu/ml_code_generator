import matplotlib.pyplot as plt
#visualize accuracy
def get_code(args):
#Accuracy Graph
   acc = args[0].history['accuracy']
   val_acc = args[0].history['val_accuracy']
   plt.figure(figsize=(12, 4))
   plt.subplot(1, 2, 1)
   plt.plot(acc, label='Training Accuracy')
   plt.plot(val_acc, label='Validation Accuracy')
   plt.legend(loc='lower right')
   plt.xlabel("Epochs")
   plt.ylabel("Accuracy")
   plt.title('Training and Validation Accuracy')
   plt.show()

#Loss Graph
   loss = args[0].history['loss']
   val_loss = args[0].history['val_loss']
   plt.figure(figsize=(12, 5))
   plt.subplot(1, 2, 1)
   plt.plot(loss, label='Training Loss')
   plt.plot(val_loss, label='Validation Loss')
   plt.legend(loc='upper right')
   plt.xlabel("Epochs")
   plt.ylabel("Loss")
   plt.title('Training and Validation Loss')
   plt.show()

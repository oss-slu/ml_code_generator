import pandas as pd
import matplotlib.pyplot as plt
#visualize accuracy
def get_code(args):
#Accuracy Graph
   history_df = pd.DataFrame(args[0].history)
   plt.figure(figsize=(12,4))
   plt.subplot(1,2,1)
   plt.plot(history_df['loss'], label='training loss')
   plt.plot(history_df['val_loss'], label='validation loss')
   plt.title('Model Loss Function')
   plt.legend()
   plt.subplot(1,2,2)
   plt.plot(history_df['accuracy'], label='training accuracy')
   plt.plot(history_df['val_accuracy'], label='validation accuracy')
   plt.title('Model Accuracy')
   plt.legend()
   plt.show()

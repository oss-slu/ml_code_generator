import tensorflow as tf
#Finding the accuracy of the model
def get_code(args):
   precision = tf.keras.metrics.Precision()
   recall = tf.keras.metrics.Recall()
   accuracy = tf.keras.metrics.BinaryAccuracy()
   # test = args[0].map(lambda x, y: (x/255, y))
   for batch in args[0].as_numpy_iterator():
      images_batch, labels_batch = batch
      yhat = args[1].predict(images_batch)
      precision.update_state(labels_batch, yhat)
      recall.update_state(labels_batch, yhat)
      accuracy.update_state(labels_batch, yhat)
   print(f'Precision: {precision.result().numpy()}, \
   Recall: {recall.result().numpy()}, Accuracy: {accuracy.result().numpy()}')
   return precision, recall, accuracy

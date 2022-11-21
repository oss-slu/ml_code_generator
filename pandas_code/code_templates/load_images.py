import os
import tensorflow as tf
# Identifying number of classes and labels
def get_code(args):
   print(os.listdir(args[0]))
   data = tf.keras.utils.image_dataset_from_directory(args[0], batch_size=22)
   return data

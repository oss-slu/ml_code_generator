import tensorflow as tf
# Identifying number of classes and labels
def get_code(args):
   #For the configuration of using GPU
   gpus = tf.config.experimental.list_physical_devices('GPU')
   for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
   data = tf.keras.utils.image_dataset_from_directory(args[0], batch_size=22)
   return data

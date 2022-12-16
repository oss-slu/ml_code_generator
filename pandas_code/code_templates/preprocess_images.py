import tensorflow as tf
#Preprocessing images
def get_code(args):
   # Preprocess all images
   data = tf.keras.utils.image_dataset_from_directory(
      args[0],
      # validation_split=0.2,
      # subset='training',
      image_size = (256, 256),
      batch_size = 22,
      seed = 123
   )
   normalized_data = data.map(lambda x, y: (x/255, y))
   return data, normalized_data

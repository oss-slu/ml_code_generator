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
   # val_data = tf.keras.utils.image_dataset_from_directory(
   # args[0],
   # validation_split=0.2,
   # subset='validation',
   # image_size = (256, 256),
   # batch_size = 22,
   # seed = 123
   # )
   return data
   # normalization_layer = tf.keras.layers.Rescaling(1./255)
   # normalized_ds = data.map(lambda x, y: (normalization_layer(x), y))
   # return normalization_layer, data

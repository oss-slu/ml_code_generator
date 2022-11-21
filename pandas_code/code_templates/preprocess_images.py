import tensorflow as tf
#Preprocessing images
def get_code(args):
   # Preprocess all images
   train_data = tf.keras.utils.image_dataset_from_directory(
      args[0],
      validation_split=0.2,
      subset='training',
      image_size = (256, 256),
      batch_size = 22,
      seed = 123
   )
   val_data = tf.keras.utils.image_dataset_from_directory(
   args[0],
   validation_split=0.2,
   subset='validation',
   image_size = (256, 256),
   batch_size = 22,
   seed = 123
   )
   return train_data, val_data
   # normalization_layer = tf.keras.layers.Rescaling(1./255)
   # normalized_ds = data.map(lambda x, y: (normalization_layer(x), y))
   # return normalization_layer, data

# def preprocess_images(self, data_dir):
   #    # Preprocess all images
   #    data = tf.keras.utils.image_dataset_from_directory(
   #       '../'+data_dir,
   #       validation_split=0.2,
   #       subset='training',
   #       image_size = (256, 256),
   #       batch_size = 22,
   #       seed = 123
   #    )
   #    print(data)
   #    # val_data = tf.keras.utils.image_dataset_from_directory(
   #    #    '../'+data_dir,
   #    #    validation_split=0.2,
   #    #    subset='validation',
   #    #    image_size = (256, 256),
   #    #    batch_size = 22,
   #    #    seed = 123
   #    # )

   #    normalization_layer = tf.keras.layers.Rescaling(1./255)
   #    normalized_ds = data.map(lambda x, y: (normalization_layer(x), y))
   #    images_batch, labels_batch = next(iter(normalized_ds))
   #    train_class = data.class_names
   #    first_images = images_batch[0]
   #    print("Min:: ", np.min(first_images), '/n' , "Max:: ", np.max(first_images))
   #    # val_class = val_data.cl ass_names
   #    print("Train classes:: ", train_class)
   #    # print("Validation classes:: ", val_class)
   #    print("Number of training files:", len(data.file_paths))
   #    # print("Number of validation files:", len(val_data.file_paths))

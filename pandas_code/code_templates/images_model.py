import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
#Deep learning images model
def get_code(args):
   img_height = 256
   img_width = 256
   classes = args[0].class_names #data

   model = Sequential([
   tf.keras.layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
   Conv2D(16, 3, padding='same', activation='relu'),
   MaxPooling2D(),
   Conv2D(32, 3, padding='same', activation='relu'),
   MaxPooling2D(),
   Conv2D(64, 3, padding='same', activation='relu'),
   MaxPooling2D(),
   Flatten(),
   Dense(128, activation='relu'),
   Dense(len(classes))
   ])
   model.compile('adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
   model.summary()
   history = model.fit(
      args[1], #train batch
      validation_data = args[2], #validation batch
      epochs = args[3]
   )
   return history

   # def train_model(self):
   #    data = tf.keras.utils.image_dataset_from_directory("../data")
   #    img_height = 256
   #    img_width = 256
   #    classes = data.class_names
   #    model = Sequential([
   #    Rescaling(1./255, input_shape=(img_height, img_width, 3)),
   #    Conv2D(16, 3, padding='same', activation='relu'),
   #    MaxPooling2D(),
   #    Conv2D(32, 3, padding='same', activation='relu'),
   #    MaxPooling2D(),
   #    Conv2D(64, 3, padding='same', activation='relu'),
   #    MaxPooling2D(),
   #    Flatten(),
   #    Dense(128, activation='relu'),
   #    Dense(len(classes))
   #    ])
   #    model.compile('adam', loss=tf.keras.losses.SparseCategoricalCrossentropy
   # (from_logits=True), metrics=['accuracy'])
   #    model.summary()
   #    history = model.fit(
   #       train_ds,
   #       validation_data = val_ds,
   #       epochs = 10
   #    )

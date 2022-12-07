import tensorflow as tf
#Deep learning images model
def get_code(args):

   model = tf.keras.models.Sequential([
   tf.keras.layers.Conv2D(16, 3, padding='same', input_shape=(256, 256, 3), activation='relu'),
   tf.keras.layers.MaxPooling2D(),
   tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
   tf.keras.layers.MaxPooling2D(),
   tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
   tf.keras.layers.MaxPooling2D(),
   tf.keras.layers.Flatten(),
   tf.keras.layers.Dense(256, activation='relu'),
   tf.keras.layers.Dense(1, activation='sigmoid')
   ])
   early_stopping = tf.keras.callbacks.EarlyStopping\
      (monitor='val_loss', mode='min', verbose=1, patience=10)
   model.compile('adam',
               #   SparseCategoricalCrossentropy(from_logits=True)
    loss=tf.losses.BinaryCrossentropy(),metrics=['accuracy'])
   model.summary()

   history = model.fit(
      args[1], #train batch
      validation_data = args[2], #validation batch
      epochs = args[3], #change number of epochs as per your requirement
      callbacks=[early_stopping]
   )
   # model.save(os.path.join('models', 'simplemodel.h5'))
   return history, model

     # data_dir = '../data'
      # print(os.listdir(os.path.join(data_dir)))
      # data = tf.keras.utils.image_dataset_from_directory(data_dir, batch_size=12) #Dividing the data in different batches and showing labels
      # # data_iterator = data.as_numpy_iterator() # Iterating thru each batch of images
      # # batch = data_iterator.next() # Getting images of each batch
      
      # # Plotting batch of images
      # class_names = data.class_names
      # plt.figure(figsize=(10, 10))
      # for images, labels in data.take(1):  
      #    for i in range(9):
      #       ax = plt.subplot(3, 3, i + 1)
      #       plt.imshow(images[i].numpy().astype("uint8"))
      #       plt.title(class_names[labels[i]] + ' => ' + str(labels[i].numpy()))
      #       plt.axis("off")
      # plt.show()
      
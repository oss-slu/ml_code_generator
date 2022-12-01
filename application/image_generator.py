import random
import matplotlib.pyplot as plt
from application.code_parser import CodeParser
class ImageGenerator(CodeParser):
   def load_images(self, images_directory):
      #Dividing the data in different batches and showing labels
      self.\
         parse_and_execute('load_images', [images_directory])

   def validate_images(self, images_directory):
      self.\
         parse_and_execute('validate_images', [images_directory])

   def preprocess_images(self, images_directory): #directory after validating the images
      data = self.\
         parse_and_execute('preprocess_images', [images_directory])
      print("Train classes:: ", data.class_names)
      print("Number of training files:", len(data.file_paths))
      self.save('data', data)
      class_names = self.data['data'].class_names
      plt.figure(figsize=(10, 10))
      for images, labels in self.data['data'].take(random.randint(1,len(data))):
         for i in range(9):
            plt.subplot(3, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]] + ' => ' + str(labels[i].numpy()))
            plt.axis("off")
      plt.show()
      return self.data['data']

   def split_images(self, train_ratio, val_ratio, test_ratio):
      (train, val, test) = self.\
         parse_and_execute('split_images', ['data', train_ratio, val_ratio, test_ratio])
      self.save('train', train)
      self.save('val', val)
      self.save('test', test)
      return self.data['train'], self.data['val'], self.data['test']

   def train_model(self, epochs):
      history = self.\
         parse_and_execute('images_model', ['data', 'train', 'val', epochs])
      self.save('history', history)
      return self.data['history']

   def visualize(self, history):
      self.\
         parse_and_execute('visualize', ['history', history])

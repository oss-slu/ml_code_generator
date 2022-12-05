import random
import cv2
import matplotlib.pyplot as plt
from application.code_parser import CodeParser
class ImageGenerator(CodeParser):
   def load_images(self, images_directory):
      #Dividing the data in different batches and showing labels
      data = self.\
         parse_and_execute('load_images', [images_directory])
      print(data)

   def validate_images(self, images_directory):
      self.\
         parse_and_execute('validate_images', [images_directory])

   def preprocess_images(self, images_directory): #directory after validating the images
      (data, normalized_data) = self.\
         parse_and_execute('preprocess_images', [images_directory])
      class_mapping = {}
      print("Train classes:: ", data.class_names)
      print("Number of training files:", len(data.file_paths))
      self.save('data', data)
      self.save('normalized_data', normalized_data)
      class_names = self.data['data'].class_names
      plt.figure(figsize=(10, 10))
      for images, labels in self.data['data'].take(random.randint(1,len(data))):
         for i in range(9):
            plt.subplot(3, 3, i + 1)
            # plt.imshow(cv2.cvtColor(images[i].numpy().astype('uint8'), cv2.COLOR_BGR2RGB))
            plt.imshow(images[i].numpy().astype("uint8"))
            class_mapping[int(labels[i].numpy())]= class_names[labels[i]]
            plt.title(class_names[labels[i]] + ' => ' + str(labels[i].numpy()))
            plt.axis("off")
      self.save('class_mapping', class_mapping)
      plt.show()
      return self.data['data']

   def split_images(self, train_ratio, val_ratio, test_ratio):
      (train, val, test) = self.\
         parse_and_execute('split_images', ['normalized_data', train_ratio, val_ratio, test_ratio])
      self.save('train', train)
      self.save('val', val)
      self.save('test', test)
      return self.data['train'], self.data['val'], self.data['test']

   def train_model(self, epochs):
      (history, model) = self.\
         parse_and_execute('images_model', ['normalized_data', 'train', 'val', epochs])
      self.save('history', history)
      self.save('model', model)
      return self.data['history']

   def model_metrics(self):
      (pre, re, acc) = self.parse_and_execute('metrics', ['test', 'model'])
      return pre, re, acc


   def visualize(self):
      self.\
         parse_and_execute('visualize', ['history'])

   def test_image(self, location):
      self.\
         parse_and_execute('test_image', [location, 'model', 'class_mapping'])

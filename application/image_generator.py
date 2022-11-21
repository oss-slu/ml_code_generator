import matplotlib.pyplot as plt
from pandas_code.parse_template import parse_template
from pandas_code.mapping import template_mapping
from application import code_generator
from model import code_blocks
class ImageGenerator:
   def __init__(self, template_mapping, parse_template):
      self.blocks = code_blocks.AllBlocks()
      self.code_generator = code_generator.CodeGenerator(template_mapping, parse_template)
      self.function_mapping = template_mapping
      self.parse_template = parse_template
      self.data = {}
      self.train = {}
      self.val = {}
      self.test = {}

   def load_images(self, images_directory):
      #Dividing the data in different batches and showing labels
      self.data = self.code_generator._parse_and_execute('load_images', [images_directory])
      # self.data = self._parse_and_execute('load_images', [images_directory])
      print(self.data)
      return self.data

   def validate_images(self, images_directory):
      self.code_generator._parse_and_execute('validate_images', [images_directory])

   def preprocess_images(self, images_directory): #directory after validating the images
      (train_data, val_data) = self.code_generator._parse_and_execute('preprocess_images', [images_directory])
      # (train_data, val_data) = self._parse_and_execute('preprocess_images', [images_directory])
      # # data_iterator = data.as_numpy_iterator() # Iterating thru each batch of images
      # batch = data_iterator.next() # Getting images of ea
      print("Train classes:: ", train_data.class_names)
      print("Validation classes:: ", val_data.class_names)
      print("Number of training files:", len(train_data.file_paths))
      print("Number of validation files:", len(val_data.file_paths))

      self.data = train_data
      class_names = self.data.class_names
      plt.figure(figsize=(10, 10))
      for images, labels in self.data.take(1):
         for i in range(9):
            plt.subplot(3, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]] + ' => ' + str(labels[i].numpy()))
            plt.axis("off")
      plt.show()

   def split_images(self, data, train_ratio=0.7, val_ratio=0.1, test_ratio=0.1 ):
      data = self.data
      (train, val, test) = self.code_generator._parse_and_execute('split_images', [data, train_ratio, val_ratio, test_ratio])
      self.train = train
      self.val = val
      self.test = test
      print(self.train)
      self.train_model(self.data, self.train, self.val,100)

   def train_model(self, data, train, val, epochs):
      data = self.data
      train = self.train
      val = self.val
      epochs = 100
      history = self.code_generator._parse_and_execute('images_model', [data, train, val, epochs])
      return history

haris = ImageGenerator(template_mapping, parse_template)
haris.load_images('data/')
haris.code_generator.download_code()
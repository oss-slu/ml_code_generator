import sys
from application import image_generator
from pandas_code.mapping import template_mapping
from pandas_code.parse_template import parse_template

def run_generator(args):
   print(args)
   input_file = args[1]
   image_gen = image_generator.ImageGenerator(template_mapping, parse_template)
   image_gen.load_images(input_file)
   image_gen.validate_images(input_file)
   data_generator = image_gen.preprocess_images(input_file)
   print('Image classes', data_generator)
   number_of_classes=  list(data_generator.class_names)
   print(f"There are {len(number_of_classes)} number of classes")
   (train, val, test) = image_gen.split_images(0.7, 0.1, 0.1)
   print(len(train))
   print(len(val))
   print(len(test))
   history = image_gen.train_model(epochs=5)
   print(history)
   image_gen.visualize(history)
   print("\n\n\nPrinting Starts from here.\n")
   print(image_gen.download_code())

#process the arguments
if __name__ == '__main__':
   run_generator(sys.argv)

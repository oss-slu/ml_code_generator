import sys
from application import image_generator, code_generator
from pandas_code.mapping import template_mapping
from pandas_code.parse_template import parse_template

def run_generator(args):
   print(args)
   input_file = args[1]
   image_gen = image_generator.ImageGenerator(template_mapping, parse_template)
   cd_generator = code_generator.CodeGenerator(template_mapping, parse_template)
   image_classes = image_gen.load_images(input_file)
   number_of_classes=  [classes for classes in image_classes.class_names]
   print(f"There are {len(number_of_classes)} number of classes")
   image_gen.validate_images(input_file)
   data_generator = image_gen.preprocess_images(input_file)
   (train, val, test) = image_gen.split_images(data_generator, 0.7, 0.1, 0.1)
   print(len(train))
   print(len(val))
   print(len(test))
   history = image_gen.train_model(data_generator, train, val, 100)
   print(history)
   image_gen.visualize(history)
   print("Printing Starts from here.")
   print(image_gen.download())

#process the arguments
if __name__ == '__main__':
   run_generator(sys.argv)

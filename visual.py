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
   classes=  list(data_generator.class_names)
   print(f"There are {len(classes)} number of classes")
   (train, val, test) = image_gen.split_images(0.7, 0.1, 0.1)
   print(len(train))
   print(len(val))
   print(len(test))
   history = image_gen.train_model(epochs=10)
   print(history)
   image_gen.visualie()
   image_gen.model_metrzics()
   image_gen.test_image('/Users/harisalam/ml_code_generator/test/10New_Bulldog.jpeg')
   # print("\n\n\nPrinting Starts from here.\n")
   print(image_gen.download_code())

#process the arguments
if __name__ == '__main__':
   run_generator(sys.argv)

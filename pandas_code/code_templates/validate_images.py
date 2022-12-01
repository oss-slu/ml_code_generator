import os
import imghdr
from cv2 import cv2
#Validating Images in the specified directory
def get_code(args):
   image_ext = ['jpeg', 'jpg', 'bmp', 'png']
   # validate images and remove inconsistent or bad images
   for image_class in os.listdir(args[0]):
      if image_class[0] != '.':
         for image in os.listdir(os.path.join(args[0], image_class)):
            if image[0] != '.':
               image_path = os.path.join(args[0], image_class, image)
            try:
               cv2.imread(image_path)
               tip = imghdr.what(image_path)
               if tip not in image_ext:
                  print(f"Image {image_path} not in the extension list".format(image_path))
                  os.remove(image_path)
            except FileNotFoundError as file_not_found:
                  print(f"Issue with Image {image_path} because {file_not_found}".format(image_path, file_not_found))

import os
import imghdr
import cv2
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
                  f"Image not in the ext list {image_path}"
                  os.remove(image_path)
            except FileNotFoundError as file_not_found:
               f"Issue with Image {image_path} because {file_not_found}"

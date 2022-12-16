import os
import imghdr
import cv2
#Validating Images in the specified directory
def get_code(args):
   image_ext = ['jpeg', 'jpg', 'bmp', 'png']
   for image_class in os.listdir(args[0]):
      if image_class[0] != '.':
         for image in os.listdir(os.path.join(args[0], image_class)):
            if image[0] != '.':
               image_path = os.path.join(args[0], image_class, image)
            try:
               cv2.imread(image_path)
               tip = imghdr.what(image_path)
               if tip not in image_ext:
                  print(f"Bad image with invalid ext {image_path}")
                  os.remove(image_path)
               # Uncomment the following two line if you've problem validating the files
               # img_bytes = tf.io.read_file(image_path)
               # tf.io.decode_image(img_bytes)
            except IOError:
               print(f"Found bad path {image_path}")
               os.remove(image_path)

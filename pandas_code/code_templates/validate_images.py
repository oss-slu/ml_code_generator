import os
import cv2
import imghdr
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
               img = cv2.imread(image_path)
               tip = imghdr.what(image_path)
               if tip not in image_ext:
                  print("Image not in the ext listb{}".format(image_path))
                  os.remove(image_path)
            except Exception as e:
               print("Issue with Image {}".format(image_path))

# def validate_images(self, data_dir):
   #    image_ext = ['jpeg', 'jpg', 'bmp', 'png']
   #    # validate images and remove inconsistent or bad images
   #    for image_class in os.listdir(data_dir):
   #       if image_class[0] != '.':
   #          for image in os.listdir(os.path.join(data_dir, image_class)):
   #             if image[0] != '.':
   #                continue
   #             image_path = os.path.join(data_dir, image_class, image)
   #             try:
   #                img = cv2.imread(image_path)
   #                tip = imghdr.what(image_path)
   #                if tip not in image_ext:
   #                   print("Image not in the ext listb{}".format(image_path))
   #                   os.remove(image_path)
   #             except Exception as e:
   #                print("Issue with Image {}".format(image_path))
   
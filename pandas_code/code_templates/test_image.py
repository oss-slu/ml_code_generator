import cv2
import numpy as np
import tensorflow as tf
# Testing the model on images which it havn't seen before
def get_code(args):
   img = cv2.imread(args[0])
   # plt.imshow(img)
   # plt.show()
   resize = tf.image.resize(img, (256, 256))
   # plt.imshow(resize.numpy().astype('uint8'))
   # plt.show()
   # print(resize.shape)
   # We're expanding dimensions of the images because
   # our model expects batch of images
   yhat = args[1].predict(np.expand_dims(resize/255, 0))
   if yhat > 0.5:
      print(f"Predicted class is {args[2][0]}")
   else:
      print(f"Predicted class is {args[2][1]}")

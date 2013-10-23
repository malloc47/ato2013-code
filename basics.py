from skimage.data import imread
from skimage.viewer import ImageViewer
from skimage.color import rgb2grey
import numpy as np

image = imread('grumpy.jpg')
ImageViewer(image).show()

print(str(image))

# image_grey = imread('grumpy.jpg', as_grey=True)
image_grey = rgb2grey(image)
ImageViewer(image_grey).show()

print(str(image_grey))

my_image = np.asarray(

    [[255,  0  ,  255],
     [0  ,  128,  0  ],
     [255,  0  ,  255]], 

    dtype='uint8')

ImageViewer(my_image).show()

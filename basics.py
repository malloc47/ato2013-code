from skimage.data import imread
from skimage.viewer import ImageViewer

image = imread('grumpy.jpg')
viewer = ImageViewer(image)
viewer.show()

image_grey = imread('grumpy.jpg', as_grey=True)
viewer = ImageViewer(image_grey)
viewer.show()

print(str(image))
print(str(image_grey))

import numpy as np

my_image = np.asarray(

    [[255,  0  ,  255],
     [0  ,  128,  0  ],
     [255,  0  ,  255]], 

    dtype='uint8')

viewer = ImageViewer(my_image)
viewer.show()

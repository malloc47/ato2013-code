from skimage.viewer import ImageViewer
from skimage.data import imread
from skimage.filter import canny
from skimage.color import rgb2grey
import numpy as np

im = imread('hancock.png')
im_grey = rgb2grey(im)

ImageViewer(im).show()

edges = canny(im_grey, sigma=3, low_threshold=0.1, high_threshold=0.2)

ImageViewer(edges).show()

edges2 = canny(im_grey, sigma=7, low_threshold=0.1, high_threshold=0.2)

ImageViewer(filtered).show()

# deal with showing the edges on the image
red = im_grey.copy()
red[edges2 > 0] = 1
green = im_grey.copy()
green[edges2 > 0] = 0
blue = im_grey.copy()
blue[edges2 > 0] = 0

im2 = np.dstack((red,green,blue))

ImageViewer(im2).show()

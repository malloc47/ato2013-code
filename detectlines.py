from skimage.viewer import ImageViewer
from skimage.data import imread
from skimage.filter import canny
from skimage.color import rgb2grey
from skimage.morphology import remove_small_objects
import numpy as np

im = imread('hancock.png')
im_grey = rgb2grey(im)

viewer = ImageViewer(im).show()

edges = canny(im_grey, sigma=7, low_threshold=0.1, high_threshold=0.2)

ImageViewer(edges).show()

filtered = remove_small_objects(edges, 500, connectivity=2)

ImageViewer(filtered).show()

red = im_grey.copy()
red[edges > 0] = 1
green = im_grey.copy()
green[edges > 0] = 0
blue = im_grey.copy()
blue[edges > 0] = 0

im2 = np.dstack((red,green,blue))

viewer = ImageViewer(im2)
viewer.show()

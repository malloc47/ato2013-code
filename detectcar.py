# images taken from http://tutorial.simplecv.org/en/latest/examples/parking.html
from skimage.data import imread
from skimage.viewer import ImageViewer, CollectionViewer
from skimage.io import imshow, show
from skimage import img_as_float
from skimage.color import rgb2grey
from skimage.filter import threshold_otsu
from reset import reset_plots
from cv2 import GaussianBlur
from skimage.morphology import binary_dilation, disk, remove_small_objects, label
from skimage.measure import regionprops

# load files
background, current = imread('parking-background.png'), imread('parking-current.png')

# blurring
kernel = (9,9)
blur = 5

bkg = GaussianBlur(background, kernel, blur) 
cur = GaussianBlur(current, kernel, blur)

# get absolute difference between images
absdiff = abs(img_as_float(cur) - img_as_float(bkg))

grey = rgb2grey(absdiff)

# threshold automatically
thresholded = grey > threshold_otsu(grey)

dilated = binary_dilation(thresholded, disk(9))

filtered = remove_small_objects(dilated, 7000)

props = regionprops(label(filtered),properties=['BoundingBox'])

viewer = CollectionViewer([background, current, bkg, cur, absdiff, grey, thresholded, dilated, filtered])
viewer.show()
reset_plots()

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

minr, minc, maxr, maxc = props[0]['BoundingBox']

fig, ax = plt.subplots(ncols=1, nrows=1)
ax.imshow(current)
ax.add_patch(mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2))
plt.show()

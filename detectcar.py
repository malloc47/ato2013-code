# images taken from http://tutorial.simplecv.org/en/latest/examples/parking.html
from skimage.data import imread
from skimage.viewer import ImageViewer
from skimage import img_as_float
from skimage.color import rgb2grey
from skimage.filter import threshold_otsu
from cv2 import GaussianBlur
from skimage.morphology import binary_dilation, disk, remove_small_objects, label
from skimage.measure import regionprops
from reset import reset_plots
from draw import boxes

# load files
background, current = imread('parking-background.png'), imread('parking-current.png')

ImageViewer(background).show()
ImageViewer(current).show()

# blurring
kernel = (9,9)
blur = 5

bkg = GaussianBlur(background, kernel, blur) 
cur = GaussianBlur(current, kernel, blur)

ImageViewer(cur).show()

# get absolute difference between images
absdiff = abs(img_as_float(cur) - img_as_float(bkg))

ImageViewer(absdiff).show()

grey = rgb2grey(absdiff)

# threshold automatically
thresholded = grey > threshold_otsu(grey)

ImageViewer(thresholded).show()

dilated = binary_dilation(thresholded, disk(9))

ImageViewer(dilated).show()

filtered = remove_small_objects(dilated, 7000)

ImageViewer(filtered).show()

# draw box around the car
props = regionprops(label(filtered),properties=['BoundingBox'])

boxes(current,[props[0]['BoundingBox']])

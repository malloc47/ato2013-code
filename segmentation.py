from skimage.viewer import ImageViewer
from skimage import img_as_ubyte
from skimage.data import imread
from skimage.color import rgb2grey
from skimage.segmentation import slic, quickshift
from skimage.segmentation import mark_boundaries

im = imread('hancock.png')

# viewer = ImageViewer(im)
# viewer.show()

# segmented = slic(img_as_ubyte(im),n_segments=100,max_iter=1)
segmented = quickshift(img_as_ubyte(im),max_dist=15)

viewer = ImageViewer(mark_boundaries(im,segmented))
viewer.show()

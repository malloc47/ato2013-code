from skimage.data import *
from skimage.viewer import CollectionViewer

built_in_images = [
    checkerboard(),
    clock(),
    coins(),
    lena(),
    moon(),
    page(),
    text()
]

viewer = CollectionViewer(built_in_images)
viewer.show()

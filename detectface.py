import cv2
from skimage import img_as_ubyte
from skimage.data import lena
from skimage.color import rgb2grey
from skimage.viewer import ImageViewer
from draw import boxes
import matplotlib.pyplot as plt

img = img_as_ubyte(rgb2grey(lena()))

img_grey = cv2.equalizeHist(rgb2grey(img))

viewer = ImageViewer(img_grey)
plt.show()
 
cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
rects = cascade.detectMultiScale(img_grey, scaleFactor=1.1,
                                 minNeighbors=3,
                                 minSize=(20,20),
                                 flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

# x y w h -> x1 y1 x2 y2
rects[:,2:] += rects[:,:2]

boxes(img,rects)

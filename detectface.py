import cv2
import cv2.cv as cv
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
                                 flags = cv.CV_HAAR_SCALE_IMAGE)

# x y w h -> x1 y1 x2 y2
rects[:,2:] += rects[:,:2]

boxes(img,rects)

capture = cv.CaptureFromCAM(0)
frame = np.asarray(cv.QueryFrame(capture)[:,:]).copy()
frame_grey = img_as_ubyte(rgb2grey(frame))
del(capture)

viewer = ImageViewer(frame)
plt.show()

rects = cascade.detectMultiScale(frame_grey, scaleFactor=1.1,
                                 minNeighbors=3,
                                 minSize=(20,20),
                                 flags = cv.CV_HAAR_SCALE_IMAGE)
rects[:,2:] += rects[:,:2]

boxes(frame_grey,rects)

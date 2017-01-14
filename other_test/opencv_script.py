import cv2
import time
import numpy as np


# img_alternative = open("received.png", "rb").read()
# img = cv2.imread('messi.jpg')
img = cv2.imread('received.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)

img_str = cv2.imencode('.jpg', img)[1].tostring()
print("size file " + str(len(img_str)))
time.sleep(1)

nparr = np.fromstring(img_str, np.uint8)
# img_recover = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
img_recover = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

cv2.imshow('second image', img_recover)
cv2.waitKey(0)

cv2.destroyAllWindows()

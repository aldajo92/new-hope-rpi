from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
camera.resolution = (640, 480)


def capture():
    # grab an image from the camera
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    cv2.imwrite('/home/pi/example.png', image)
    rawCapture.truncate(0)


def capture_string():
    # grab an image from the camera
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array

    img_str = cv2.imencode('.jpg', image)[1].tostring()
    rawCapture.truncate(0)
    return img_str


def capture_string_b64():
    # grab an image from the camera
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array

    cv2.imwrite('taked.jpg', image)
    rawCapture.truncate(0)

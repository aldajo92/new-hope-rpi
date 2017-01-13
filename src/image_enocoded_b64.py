import cv2
import base64


def read_image(name):
    return cv2.imread(name + '.jpg')


def to_b_64(frame):
    cnt = cv2.imencode('.png', frame)[1]
    return base64.encodestring(cnt)


string = to_b_64(read_image('messi'))

print string
import serial
import time
import base64
import cv2

PORT = "/dev/ttyAMA0"
BAUD = 9600


def connect():
    return serial.Serial(PORT, BAUD)


def read_image(name):
    return cv2.imread(name + '.jpg')


def to_b_64(frame):
    cnt = cv2.imencode('.png', frame)[1]
    return base64.encodestring(cnt)


serial_port = connect()
serial_port.flushInput()
serial_port.flushOutput()
string = to_b_64(read_image('messi'))
splitted = string.split("\n")

try:
    for s in splitted:
        serial_port.write(s + "\r\n")
        # print s

except KeyboardInterrupt:
    print "closing..."
    exit(0)

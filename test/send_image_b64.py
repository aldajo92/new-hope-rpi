import cv2
import base64
import serial
import time

PORT = "/dev/cu.SLAB_USBtoUART"
BAUD = 9600
serial_port = None


def connect():
    return serial.Serial(PORT, BAUD)


def send_data(string_data):
    serial_port.write(string_data)


def send_data_ln(string_data):
    send_data(string_data + "\n")


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
# for i in range(0, 2):
#     serial_port.write(splitted[i] + "\r\n")
#     time.sleep(2)
counter = 0
for s in splitted:
    serial_port.write(s + "\r\n")
    if counter % 900 == 0:
        # serial_port.flushInput()
        serial_port.flushOutput()
    print str(counter) + " " + str(len(splitted))
    counter += 1
    # serial_port.flushInput()

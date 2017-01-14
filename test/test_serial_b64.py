import serial
import time
import base64

PORT = "/dev/ttyAMA0"
BAUD = 230400 #460800


def connect():
    return serial.Serial(PORT, BAUD)


def to_b_64(name):
    with open(name + '.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string


serial_port = connect()
serial_port.flushInput()
serial_port.flushOutput()
img_str = to_b_64('messi')

try:
    img_str += "\r\n"
    print "sending..."
    # serial_port.write("IMG|" + str(len(img_str)) + "\n")
    serial_port.write(img_str)
    print img_str

except KeyboardInterrupt:
    print "closing..."
    exit(0)

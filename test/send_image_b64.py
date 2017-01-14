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


def to_b_64(name):
    with open(name + '.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string


serial_port = connect()
serial_port.flushInput()
serial_port.flushOutput()
image_string = to_b_64('messi')

counter = 0
for s in splitted:
    serial_port.write(s + "\r\n")
    if counter % 900 == 0:
        # serial_port.flushInput()
        serial_port.flushOutput()
    print str(counter) + " " + str(len(splitted))
    counter += 1
    # serial_port.flushInput()

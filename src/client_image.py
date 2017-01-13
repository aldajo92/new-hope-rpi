import threading
import serial
import time
import cv2
import numpy as np
from PIL import Image

PORT = "/dev/cu.usbmodem1421"
BAUD = 115200
serial_port = None

thread = None


def send_data(string_data):
    serial_port.write(string_data)


def send_data_ln(string_data):
    send_data(string_data + "\n")


def save_image(img_str):
    n_parr = np.fromstring(img_str, np.uint8)
    # img_recover = cv2.imdecode(n_parr, cv2.CV_LOAD_IMAGE_COLOR)
    img_recover = cv2.imdecode(n_parr, cv2.IMREAD_COLOR)
    cv2.imwrite('received.jpg', img_recover)

    # jpg = Image.fromarray(img_recover)
    # data = np.asarray(jpg)
    # jpg = Image.fromarray(np.roll(data, 1, axis=-1))
    jpg = Image.open('received.jpg')
    jpg.show()


def camera(value):
    size = int(value)
    image_buffer = ""
    while True:
        image_buffer = image_buffer + serial_port.read(1)
        if len(image_buffer) == size:
            break
    save_image(image_buffer)
    serial_port.flushInput()
    serial_port.flushOutput()
    print "completed..."


def print_date():
    print "this is a date"


def parse_command(command):
    print command[0]
    if command[0] == "CAM":
        print command[1]
        camera(command[1])
    elif command[0] == "DATE":
        print_date()


def handle_data(data):
    local_data = data.split('\n')
    if local_data[0] == "hello...":
        print "ready..."
        send_data_ln("CAM")
    else:
        split_data = local_data[0].split("|")
        parse_command(split_data)


def read_from_port():
    while True:
        reading = serial_port.readline()
        if reading != "" and reading != " ":
            handle_data(reading)


def main():
    global thread
    thread = threading.Thread(target=read_from_port)
    thread.start()
    send_data_ln("HEL")


try:
    while True:
        try:
            serial_port = serial.Serial(PORT, BAUD)
        except serial.SerialException:
            print "trying..."
            time.sleep(2)
            continue
        break

    print "connected..."
    main()

except KeyboardInterrupt:
    print "clean"
    exit(0)

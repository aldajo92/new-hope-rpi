import RPi.GPIO as GPIO
import time
import serial
import base64
import pi_capture
import requests

INPUT_1 = 11
INPUT_2 = 12
INPUT_3 = 13
INPUT_4 = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(INPUT_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(INPUT_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(INPUT_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(INPUT_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

PORT = "/dev/ttyAMA0"
BAUD = 230400
serial_port = None
BASE_URL = "https://the-skywalkers.herokuapp.com"


def connect():
    return serial.Serial(PORT, BAUD)


def send_data(string_data):
    serial_port.write(string_data)


def send_data_ln(string_data):
    send_data(string_data + "\r\n")


def my_callback_1(channel):
    pi_capture.capture_string_b64()
    img_str = to_b_64('taked')
    str_response = encode_feature_1(post_image(img_str))
    print(str_response)
    # print("Feature1")


def my_callback_2(channel):
    send_data_ln("Feature4")


def my_callback_3(channel):
    send_data_ln("Feature2")


def my_callback_4(channel):
    send_data_ln("Feature3")


def encode_feature_1(value):
    return "Feature1" + value


def to_b_64(name):
    with open(name + '.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string


def post_image(image_str):
    url = BASE_URL + "/api/v1/image"
    data = {'id': 'abc123', 'base64': image_str}
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data, headers).content
    return response


GPIO.add_event_detect(INPUT_1, GPIO.RISING, callback=my_callback_1, bouncetime=500)
GPIO.add_event_detect(INPUT_2, GPIO.RISING, callback=my_callback_2, bouncetime=500)
GPIO.add_event_detect(INPUT_3, GPIO.RISING, callback=my_callback_3, bouncetime=500)
GPIO.add_event_detect(INPUT_4, GPIO.RISING, callback=my_callback_4, bouncetime=500)

try:
    serial_port = connect()
    serial_port.flushInput()
    serial_port.flushOutput()

    print "press something"
    while True:
        # print "hello"
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()  # clean up GPIO on CTRL+C exit
    serial_port.close()
GPIO.cleanup()  # clean up GPIO on normal exit

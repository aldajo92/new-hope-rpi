import requests
import base64
import serial
# import RPi.GPIO as GPIO

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


def encode_feature_1(value):
    return "Feature1" + value


def to_b_64(name):
    with open(name + '.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string


img_str = to_b_64('messi')


def post_image(image_str):
    url = BASE_URL + "/api/v1/image"
    data = {'id': 'abc123', 'base64': image_str}
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data, headers).content
    return response


try:
    # serial_port = connect()
    # serial_port.flushInput()
    # serial_port.flushOutput()
    str_response = encode_feature_1(post_image(img_str))
    # send_data_ln(str_response)
    print str_response
except KeyboardInterrupt:
    # GPIO.cleanup()  # clean up GPIO on CTRL+C exit
    serial_port.close()
# GPIO.cleanup()  # clean up GPIO on normal exit

import RPi.GPIO as GPIO
import time
import serial
import pi_capture

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


def connect():
    return serial.Serial(PORT, BAUD)


def send_data(string_data):
    serial_port.write(string_data)


def send_data_ln(string_data):
    send_data(string_data + "\r\n")


def my_callback_1(channel):
    pi_capture.capture_string_b64()
    print("Feature1")


def my_callback_2(channel):
    send_data_ln("Feature4")


def my_callback_3(channel):
    send_data_ln("Feature2")


def my_callback_4(channel):
    send_data_ln("Feature3")


GPIO.add_event_detect(INPUT_1, GPIO.RISING, callback=my_callback_1, bouncetime=300)
GPIO.add_event_detect(INPUT_2, GPIO.RISING, callback=my_callback_2, bouncetime=300)
GPIO.add_event_detect(INPUT_3, GPIO.RISING, callback=my_callback_3, bouncetime=300)
GPIO.add_event_detect(INPUT_4, GPIO.RISING, callback=my_callback_4, bouncetime=300)

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

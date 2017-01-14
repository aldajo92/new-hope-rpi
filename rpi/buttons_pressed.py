import RPi.GPIO as GPIO
import time

INPUT_1 = 11
INPUT_2 = 12
INPUT_3 = 13
INPUT_4 = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(INPUT_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(INPUT_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(INPUT_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(INPUT_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def my_callback_1(channel):
    print "falling edge detected on 17"


def my_callback_2(channel):
    print "falling edge detected on 23"


def my_callback_3(channel):
    print "falling edge detected on 23"


def my_callback_4(channel):
    print "falling edge detected on 23"


GPIO.add_event_detect(INPUT_1, GPIO.RISING, callback=my_callback_1, bouncetime=300)
GPIO.add_event_detect(INPUT_2, GPIO.RISING, callback=my_callback_2, bouncetime=300)
GPIO.add_event_detect(INPUT_3, GPIO.RISING, callback=my_callback_3, bouncetime=300)
GPIO.add_event_detect(INPUT_4, GPIO.RISING, callback=my_callback_4, bouncetime=300)

try:
    print "press something"
    while True:
        print "hello"
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()  # clean up GPIO on CTRL+C exit
GPIO.cleanup()  # clean up GPIO on normal exit

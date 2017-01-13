import serial
import time

PORT = "/dev/ttyAMA0"
BAUD = 115200


def connect():
    return serial.Serial(PORT, BAUD)


serial_port = connect()

try:
    while True:
        serial_port.write("hello" + "\r\n")
        print "hello"
        time.sleep(0.5)

except KeyboardInterrupt:
    print "closing..."
    exit(0)

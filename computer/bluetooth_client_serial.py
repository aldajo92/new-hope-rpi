import threading
import serial
import time

PORT = "/dev/tty.HC-05-DevB"
BAUD = 460800
serial_port = None

thread = None
image_buffer = ""





def read_from_port():
    while True:
        reading = serial_port.readline()
        if reading != "" and reading != " ":
            print reading


def main():
    global thread
    thread = threading.Thread(target=read_from_port)
    thread.start()


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
    serial_port.flushInput()
    serial_port.flushOutput()
    main()

except KeyboardInterrupt:
    print "clean"
    exit(0)

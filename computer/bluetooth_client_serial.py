import threading
import serial
import time

PORT = "/dev/tty.HC-05-DevB"
BAUD = 460800
serial_port = None

thread = None


def convert_image(data):
    size = int(data)
    image_buffer = ""
    while True:
        image_buffer = image_buffer + serial_port.read(1)
        if len(image_buffer) == size:
            break

    print str(len(image_buffer))


def parse_command(command):
    local_data = command.split('\n')
    s_command = local_data[0].split("|")
    if s_command[0] == "IMG":
        convert_image(s_command[1])


def read_from_port():
    while True:
        reading = serial_port.readline()
        if reading != "" and reading != " ":
            parse_command(reading)


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

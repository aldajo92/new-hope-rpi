# new-hope-rpi

### Dependencies. ###

Its necessary to enable the pi-camera with `sudo raspi-config`, and install the following packages to run this python project on RPi:

```
~$ sudo apt-get update
~$ sudo apt-get install python-pip
~$ sudo apt-get install python2.7-dev
~$ sudo apt-get install python-picamera
~$ pip install "picamera[array]"
~$ sudo pip install "picamera[array]" --upgrade
~$ sudo apt-get install python-PIL -y
~$ sudo apt-get install libopencv-dev python-opencv -y
~$ sudo apt-get install requests --upgrade
```

If there are a problem with OpenCV with dependencies:
```
~$ sudo apt-get -f install
~$ sudo apt-get install libopencv-dev python-opencv -y
```

After installation ends, reboot system with `sudo reboot`.

Install after serial communication library:

```
~$ sudo apt-get install python-serial
```

(alternative)

```
~$ python -m pip install pyserial
```

### Rpi pins
We are using the following pins on Raspberry Pi:
INPUT_1 = 11
INPUT_2 = 12
INPUT_3 = 13
INPUT_4 = 15
RX = 8
TX = 10

![alt tag](http://www.electronics-lab.com/wp-content/uploads/2014/07/GPIO.png)

### Bluetooth module in at mode
http://www.martyncurrey.com/arduino-with-hc-05-bluetooth-module-at-mode/
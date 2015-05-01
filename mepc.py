import RPi.GPIO as GPIO

# setup control motors (refernce top down view)
GPIO.setup(11, GPIO.out)  # top left
GPIO.setup(13, GPIO.out)  # top right
GPIO.setup(15, GPIO.out)  # bottom left
GPIO.setup(16, GPIO.out)  # bottom right

GPIO.setup(3, GPIO.out)  # main thrust motor
GPIO.setup(5, GPIO.out)  # x axis of MAME (multi axis mid engine)
GPIO.setup(7, GPIO.out)  # y axis of MAME (multi axis mid engine)

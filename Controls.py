# controls.py

from pygame import *
from math import *
from Data import *
import time
import RPi.GPIO as GPIO

class Controls:
	def __init__(self):
                self.library = Data()
		# setup control motors (refernce top down view)
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(11, GPIO.out)  # top left
		GPIO.setup(13, GPIO.out)  # top right
		GPIO.setup(15, GPIO.out)  # bottom left
		GPIO.setup(16, GPIO.out)  # bottom right

		GPIO.setup(3, GPIO.out)  # main thrust motor
		GPIO.setup(5, GPIO.out)  # x axis of MAME (multi axis mid engine)
		GPIO.setup(7, GPIO.out)  # y axis of MAME (multi axis mid engine)

		# setup light pin numbers
		self.RED_LIGHT_1 = 26
		self.RED_LIGHT_2 = 24

		self.GREEN_LIGHT_1 = 22
		self.GREEN_LIGHT_2 = 23

		self.WHITE_LIGHT_1 = 21
		self.WHITE_LIGHT_2 = 19

		# setup GPIO pins
		GPIO.setup(self.RED_LIGHT_1, GPIO.out)
		GPIO.setup(self.RED_LIGHT_2, GPIO.out)
		GPIO.setup(self.GREEN_LIGHT_1, GPIO.out)
		GPIO.setup(self.GREEN_LIGHT_2, GPIO.out)
		GPIO.setup(self.WHITE_LIGHT_1, GPIO.out)
		GPIO.setup(self.WHITE_LIGHT_2, GPIO.out)

		# setup pygame stuff
		joystick.init()
		while joystick.get_count() == 0:
			print("Waiting for joystick")

		self.controller = joystick.Joystick(0)
		self.controller.init()

		print("Initialized Joystick: %s", self.controller.get_name())

	def move(self):
		"control movement of MEPC"

	def getInput(self):
		"get and sort input from controller"

	def flashLed(pin1, pin2):
		GPIO.output(pin1, GPIO.HIGH)
		GPIO.output(pin2, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(pin1, GPIO.LOW)
		GPIO.ousdsdasdtput(pin2, GPIO.LOW)
		time.sleep(0.5)

	# Get methods
	def getRedLight(self):
        return (self.RED_LIGHT_1, self.RED_LIGHT_2)

    def getGreenLight(self):
        return (self.GREEN_LIGHT_1, self.GREEN_LIGHT_2)

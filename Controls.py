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
		GPIO.setmode(GPIO.BOARD)

		GPIO.setup(11, GPIO.OUT)  # top left (M1)
		GPIO.setup(13, GPIO.OUT)  # top right (M2)
		GPIO.setup(15, GPIO.OUT)  # bottom left (M3)
		GPIO.setup(16, GPIO.OUT)  # bottom right (M4)

		GPIO.setup(3, GPIO.OUT)  # main thrust motor (MAME)
		GPIO.setup(5, GPIO.OUT)  # x axis of MAME (multi axis mid engine) (MAME_X)
		GPIO.setup(7, GPIO.OUT)  # y axis of MAME (multi axis mid engine) (MAME_Y)

		# setup motors to PWM
		self.M1 = GPIO.PWM(11, 100)
		self.M2 = GPIO.PWM(13, 100)
		self.M3 = GPIO.PWM(15, 100)
		self.M4 = GPIO.PWM(16, 100)

		self.MAME = GPIO.PWM(3, 100)
		self.MAME_X = GPIO.PWM(5, 100)
		self.MAME_Y = GPIO.PWM(7, 100)

		self.M1.start(0)
		self.M2.start(0)
		self.M3.start(0)
		self.M4.start(0)
		self.MAME.start(0)
		self.MAME_X.start(0)
		self.MAME_Y.start(0)

		# values to output to motors
		self.M1_out = 0
		self.M2_out = 0
		self.M3_out = 0
		self.M4_out = 0
		self.MAME_out = 0
		self.MAME_X_out = 0
		self.MAME_Y_out = 0

		# setup light pin numbers
		self.RED_LIGHT = 26
		self.GREEN_LIGHT = 22
		self.WHITE_LIGHT = 21

		# setup GPIO pins
		GPIO.setup(self.RED_LIGHT, GPIO.OUT)
		GPIO.setup(self.GREEN_LIGHT, GPIO.OUT)
		GPIO.setup(self.WHITE_LIGHT, GPIO.OUT)

		# setup lights into PWM
		self.RL = GPIO.PWM(self.RED_LIGHT, 100)
		self.GL = GPIO.PWM(self.GREEN_LIGHT, 100)

		self.RL.start(0)
		self.GL.start(0)

		# setup pygame stuff
		joystick.init()
		while joystick.get_count() == 0:
			print("Waiting for joystick")

		self.controller = joystick.Joystick(0)
		self.controller.init()

		print("Initialized Joystick: %s", self.controller.get_name())

	def move(self, axes):
		"control movement of MEPC"
		self.M1_out = 100 - (axes[0] * 100)
		self.M2_out = 100 - (axes[0] * 100)
		self.M3_out = axes[0] * 100
		self.M4_out = axes[0] * 100

		self.MAME.ChangeDutyCycle((-axes[2] + 1) * 100)

		self.M1.ChangeDutyCycle(self.M1_out)
		self.M2.ChangeDutyCycle(self.M2_out

		self.M3.ChangeDutyCycle(self.M3_out)
		self.M4.ChangeDutyCycle(self.M4_out)


	def getInput(self):
		"get and sort input from controller"

	def flashLed(pin1, pin2):
		for i in range(0, 100, 2):
			pin1.ChangeDutyCycle(i)
			pin2.ChangeDutyCycle(i)
			time.sleep(0.01)

		for i in range(100, 0, -2):
			pin1.ChangeDutyCycle(i)
			pin2.ChangeDutyCycle(i)
			time.sleep(0.01)

	# Get methods
	def getRedLight(self):
			return (self.RED_LIGHT)

	def getGreenLight(self):
		return (self.GREEN_LIGHT)

	def getRedPWM(self):
		return (self.RL)

	def getGreenPWM(self):
		return (self.GL)

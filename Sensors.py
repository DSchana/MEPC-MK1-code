# Sensors.py

import RPi.GPIO as GPIO
from pygame import *
from Data import *
from MPU6050 import *
from PID import *

class Sensors:
	def __init__(self):
		"Set up the Sensors stuff here"
		# QUSTIONABLE
		self.address = 0x68  # This is the address value read via the i2cdetect command
		self.bus = smbus.SMBus(1)
		self.gyro = MPU6050(bus, address, "MPU6050")

		self.library = Data()
		self.ultra_front_data = "put stuff here"
		self.ultra_top_data = "put stuff here"
		self.ultra_bottom_data = "put stuff here"
		self.gyro_data = []  # put stuff here (list)

		self.ULTRA_FRONT_PIN = "number"
		self.ULTRA_TOP_PIN = "number"
		self.ULTRA_BOTTOM_PIN = "number"
		self.GYRO_PIN = "number"

		joystick.init()
		self.controller = joystick.Joystic(0)
		self.controller.init()
		self.axes = self.controller.get_numaxes()

	# get methods
	def getPins(self):
				return (slef.ULTRA_FRONT_PIN, self.ULTRA_TOP_PIN,
						self.ULTRA_BOTTOM_PIN, self.GYRO_PIN)

	def getData(self):
			return (self.ultra_front_data, self.ultra_top_data,
					self.ultra_bottom_data, self.gyro_data)

	def getAxis(self):
		axes_return = []
		for i in range(self.axes):
			axes_return.append(self.controller.get_axis(i))
		return axes_return
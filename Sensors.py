# Sensors.py

import RPi.GPIO as GPIO

class Sensors:
	def __init__(self):
		"Set up the Sensors stuff here"
		self.ultra_front_data = "put stuff here"
		self.ultra_top_data = "put stuff here"
		self.ultra_bottom_data = "put stuff here"
		self.gyro_data = "put stuff here"

		self.ULTRA_FRONT_PIN = "number"
		self.ULTRA_TOP_PIN = "number"
		self.ULTRA_BOTTOM_PIN = "number"
		self.GYRO_PIN = "number"
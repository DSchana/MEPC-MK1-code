import sys
import time
import os
import RPi.GPIO as GPIO
from pygame import *
from Data import *

# setup classes
library = Data()
controls = library.getControls()
sensors = library.getSensors()
brains = library.getAI()

running = True

while running:
	for e in event.get():
		if e.type == QUIT:
			running = False

	controls.flashLed(controls.getRedPWM(), controls.getGreenPWM())

	controls.move(sensors.getAxis())

quit()
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
	controls.flashLed(controls.getRedLight[0], controls.getRedLight[1])
	controls.flashLed(controls.getGreenLight[0], controls.getGreenLight[1])

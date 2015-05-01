import sys
import time
import os
import RPi.GPIO as GPIO
from pygame import *
from Controls import *
from Sensors import *

# setup classes
controls = Controls()
sensors = Sensors()

running = True

while running:
	flashLed(RED_LIGHT_1, RED_LIGHT_2)
	flashLed(GREEN_LIGHT_1, GREEN_LIGHT_2)

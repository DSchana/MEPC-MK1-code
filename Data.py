# Data.py
from Controls import *
from Sensors import *
from AI import *

class Data:
    def __init__(self):
        self.controls = Controls()
        self.sensors = Sensors()
        self.brains = AI()

    def getControls(self):
        return self.controls

    def getSensors(self):
        return self.sensors

    def getAI(self):
        return self.brains

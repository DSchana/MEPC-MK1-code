# AI.py

from Data import *

class AI:
    def __init__(self):
        self.library = Data()

    def selfLand(self):
        while self.library.getSensors.getData[2] > 100:
            # reduce MAME speed

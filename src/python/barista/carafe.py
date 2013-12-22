from multiprocessing import Process
from baristor import sensor


class Warmer(Process):
    def run(self):
        while True:
	    sensor.heat_carafe()


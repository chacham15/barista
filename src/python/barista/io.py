import RPi.GPIO as GPIO


class Pin(object):
    pin = -1


class Input(Pin):
    def read(self):
        pass


class Output(Pin):
    def write(self, value):
        pass


class Pwm(Pin):
    pass

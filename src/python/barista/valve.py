from barista.pin import Pin


class Valve(Pin):
    pin = -1

    def open(self):
        super(Valve, self).high()

    def close(self):
        super(Valve, self).low()


ulass SoluteValve(Valve):
    pin = 1


class SolventValve(Valve):
    pin = 2


class CarafeValve(Valve):
    pin = 3


class WaterPumpInletValve(Valve):
    pin = 4


class WaterPumpExitValve(Vavle):
    pin = 5


from barista.io import Output


class Valve(Output):
    pin = -1

    def open(self):
        super(Valve, self).high()

    def close(self):
        super(Valve, self).low()


class CoffeeOutlet(Valve):
    pass


class WaterInlet(Valve):
    pass


class WaterPumpInlet(Valve):
    pass


class WaterPumpOutlet(Valve):
    pass


class BrewOutlet(Valve):
    pass

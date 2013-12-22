from barista.sensor import BrewTemp


class Brew(object):
    def __init__(self):
        self.temp = BrewTemp()

from barista.sensor import CarafeLevel, CarafeTemp


class Carafe(object):
    def __init__(self):
        self.level = CarafeLevel()
        self.temp = CarafeTemp()

    # TODO add callback for when the temperature or level are too low.
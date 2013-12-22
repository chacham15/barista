from barista.pin import Pin


class Motor(Pin):
    def start(self):
        super(Motor, self).high()

    def stop(self):
        super(Motor, self).low()


class WaterPump(Motor):
    pass


class WastePump(Motor):
    pass

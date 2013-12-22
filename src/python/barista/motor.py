from barista.io import Output


class Motor(Output):
    def start(self):
        super(Motor, self).write(True)

    def stop(self):
        super(Motor, self).write(False)


class WaterPump(Motor):
    pass


class WastePump(Motor):
    pass

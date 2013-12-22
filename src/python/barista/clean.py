from barista.motor import WaterPump, WastePump

class Clean(object):
    def __init__(self):
        self.water = WaterPump()
        self.waste = WastePump()

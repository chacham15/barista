import time
from barista import brew, clean, sensor


def main():
    while True:
        if sensor.carafe_is_low():
            brew()
            clean()
        time.sleep(10)


from display import Display
from machine import RTC

DEFAULT_TIME = (2022, 11, 1, 0, 0, 0, 0, 0)


class Watchy:
    def __init__(self):
        self.display = Display()
        self.rtc = RTC()
        self.rtc.init(DEFAULT_TIME)
        pass

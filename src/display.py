from epaper1in54 import EPD
from machine import Pin, SPI
import framebuf


class Display:

    BACKGROUND = 0
    FOREGROUND = 1

    MAX_WIDTH = 200
    MAX_HEIGHT = 200

    def __init__(self):
        cs = Pin(5, Pin.OUT, value=1)
        dc = Pin(10, Pin.OUT, value=0)
        reset = Pin(9, Pin.OUT, value=0)
        busy = Pin(19, Pin.IN)

        sck = Pin(18)
        mosi = Pin(23)
        miso = Pin(19)  # appears not to be used but is mandatory

        spi = SPI(
            1,
            baudrate=20000000,
            polarity=0,
            sck=sck,
            mosi=mosi,
            miso=miso,
        )
        self.epd = EPD(spi=spi, cs=cs, dc=dc, rst=reset, busy=busy)
        self.current_x = 0
        self.current_y = 0
        self.buffer = bytearray(self.MAX_WIDTH * self.MAX_HEIGHT // 8)
        self.framebuf = framebuf.FrameBuffer(
            self.buffer, self.MAX_WIDTH, self.MAX_HEIGHT, framebuf.MONO_HLSB
        )
        self.epd.init()
        self.epd.hw_init()

    def update(self, buffer: bytearray = None):
        self.epd.write_buffer_to_ram(self.buffer if buffer is None else buffer)

    def fill(self, color: int):
        self.framebuf.fill(color)
        self.update()

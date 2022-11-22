import esp32
import time
from machine import Pin
from constants import VIBRATE_MOTOR_PIN


def get_temperature() -> float:
    """Returns the temperature detected by the MCU in Celsius"""
    return (esp32.raw_temperature() - 32) / 1.8


def vibrate_motor(intervals_ms):
    """
    Vibrates for the specified intervals (to be provided in milliseconds)
    intervals should be provided in the following format: [VIBRATE, DELAY, VIBRATE, etc.]
    """
    vibrate_pin = Pin(VIBRATE_MOTOR_PIN, Pin.OUT)
    vibrate_on: bool = False
    for i in intervals_ms:
        vibrate_on = not vibrate_on
        vibrate_pin.value(vibrate_on)
        time.sleep_ms(i)  # type: ignore
    vibrate_pin.off()

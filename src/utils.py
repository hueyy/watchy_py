import esp32
import time
from machine import Pin
from typing import List

def get_temperature() -> float:
  """ Returns the temperature detected by the MCU in Celsius """
  return (esp32.raw_temperature()- 32) / 1.8

def vibrate_motor(intervals_ms: List[float]):
  """
  Vibrates for the specified intervals (to be provided in milliseconds)
  intervals should be provided in the following format: [VIBRATE, DELAY, VIBRATE, etc.]
  """
  VIB_MOTOR_PIN = 13
  vibrate_pin = Pin(13, Pin.OUT)
  vibrate_on: bool = False
  for i in intervals_ms:
    vibrate_on = not vibrate_on
    vibrate_pin.value(vibrate_on)
    time.sleep_ms(i)
  vibrate_pin.off()
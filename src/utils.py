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
    :param intervals_ms: intervals should be provided in the following format: [VIBRATE, DELAY, VIBRATE, etc.]
    """
    vibrate_pin = Pin(VIBRATE_MOTOR_PIN, Pin.OUT)
    vibrate_on: bool = False
    for i in intervals_ms:
        vibrate_on = not vibrate_on
        vibrate_pin.value(vibrate_on)
        time.sleep_ms(i)  # type: ignore
    vibrate_pin.off()


NUMBER_SINGLES = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def hour_to_string(hour: int) -> str:
    """
    :param hour: expects a number between 0 and 12 (inclusive)
    """
    HOURS = ["twelve"]
    HOURS.extend(NUMBER_SINGLES)
    HOURS.extend(["ten", "eleven"])
    return HOURS[hour % 12]


def number_teen_to_string(number: int) -> str:
    """
    :param number: expects a number between 1 and 19 (inclusive)
    """
    NUMBERS = NUMBER_SINGLES.extend(
        [
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ]
    )
    return NUMBERS[number - 1]


def number_tens_to_string(number: int) -> (str, str):
    """
    :param number: expects a number between 20 and 59 (inclusive)
    """
    NUMBER_TENS = ["twenty", "thirty", "forty", "fifty"]
    tens = number // 10
    singles = number % 10
    NUMBER_ONES = [""]
    NUMBER_ONES.extend(NUMBER_SINGLES)
    return (NUMBER_TENS[tens - 2], NUMBER_ONES[singles])


def month_to_short_string(number: int) -> str:
    """
    :param number: 1 - 12 for January till December
    """
    MONTH_SHORT_STRINGS = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec",
    ]
    return MONTH_SHORT_STRINGS[number - 1]


def week_day_to_short_string(number: int) -> str:
    """
    :param number: 1 - 7 for Monday till Sunday
    """
    WEEK_DAY_SHORT_STRINGS = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    return WEEK_DAY_SHORT_STRINGS[number - 1]

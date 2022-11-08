from display import Display
from images import dino
from utils import vibrate_motor

d = Display()
d.update(dino)

vibrate_motor([500])  # done

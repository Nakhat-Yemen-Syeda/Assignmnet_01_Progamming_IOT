from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = (255, 255, 0) #Yellow
b = (0, 0, 0) # Black
p=(204,0,102)#pink
r=(204,0,0)#red

happy_emoji = [
   p, p, p, p, p, p, p, p,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, b, b, y, y, b, b, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, y, y, b, b, y, y, y,
   p, p, p, y, y, p, p, p
]

angry_emoji= [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, r, r, y, y, r, r, y,
   y, r, r, y, y, r, r, y,
   y, y, y, y, y, y, y, y,
   y, y, y, b, b, y, y, y,
   y, y, b, y, y, b, y, y,
   y, b, y, y, y, y, b, y
]
heart_emoji= [
   b, r, y, y, y, y, r, b,
   r, y, r, y, y, r, r, r,
   r, y, y, r, r, y, y, r,
   r, y, y, r, r, y, y, r,
   r, y, y, y, y, y, y, r,
   y, r, y, y, y, y, r, y,
   y, y, r, y, y, r, y, y,
   y, b, y, y, r, y, b, y
]


while True:
   sense.set_pixels(happy_emoji)
   sleep(3)
   sense.set_pixels(angry_emoji)
   sleep(3)
   sense.set_pixels(heart_emoji)
   sleep(10)
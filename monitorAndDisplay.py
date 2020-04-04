import json
from sense_hat import SenseHat

f=open('/home/pi/Desktop/config.json' ,'r')
s=f.read()
temp=json.loads(s)
sense = SenseHat()
t = sense.get_temperature()
t = round(t, 1)

coldMax = temp["cold_max"]
comfortableMin = temp["comfortable_min"]
comfortableMax = temp["comfortable_max"]
hotMin = temp["hot_min"]

r = (255,0,0)
g = (0,255,0)
b = (0,0,255)
message = "Temperature: " + str(t)

if (t<=coldMax):
    sense.show_message(message, scroll_speed=0.10, text_colour=b)
    
elif (t>comfortableMin) and (t<comfortableMax):
    sense.show_message(message, scroll_speed=0.10, text_colour=g)
    
else:
    sense.show_message(message, scroll_speed=0.10, text_colour=r)

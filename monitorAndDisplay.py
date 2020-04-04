import json
from sense_hat import SenseHat
from time import sleep
from threading import Timer
from threading import Thread

class Temperature:
    
    def __init__(self):
        self.sense = SenseHat()
        self.temp = 0
        self.r = (255,0,0)
        self.g = (0,255,0)
        self.b = (0,0,255)
        
        f=open('/home/pi/Desktop/assignment/config.json' ,'r')
        s=f.read()
        temp=json.loads(s)

        self.coldMax = temp["cold_max"]
        self.comfortableMin = temp["comfortable_min"]
        self.comfortableMax = temp["comfortable_max"]
        self.hotMin = temp["hot_min"]
        
    def setTemp(self):
        self.temp = self.sense.get_temperature()-20.0
        self.temp = round(self.temp, 1)
        
    def printMsg(self):
        self.setTemp()
        
        message = "Temperature: " + str(self.temp)

        if (self.temp<=self.coldMax):
            self.sense.show_message(message, scroll_speed=0.10, text_colour=self.b)
            
        elif (self.temp>self.comfortableMin) and (self.temp<self.comfortableMax):
            self.sense.show_message(message, scroll_speed=0.10, text_colour=self.g)
            
        else:
            self.sense.show_message(message, scroll_speed=0.10, text_colour=self.r)
            
   
    def count(self):
           sleep(5)
           self.sense.clear()
           print("Here")
           
        
currentTemp = Temperature()


while True:
    t1 = Thread(target = currentTemp.count)
    t1.start()
    sleep(2)
    currentTemp.printMsg()
    

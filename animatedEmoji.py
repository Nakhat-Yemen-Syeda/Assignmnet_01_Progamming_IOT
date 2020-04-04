from sense_hat import SenseHat
from time import sleep

class Smiley:
    
    def __init__(self):
        self.sense= SenseHat()
        self.y = (255,255,0)
        self.r = (255, 0, 0)
        self.b = (0, 0, 0)
        self.w = (255,255,255)

        self.image = [
        self.y,self.y,self.y,self.y,self.y,self.y,self.y,self.y,
        self.y,self.y,self.y,self.y,self.y,self.y,self.y,self.y,
        self.y,self.y,self.y,self.y,self.y,self.y,self.y,self.y,
        self.y,self.y,self.y,self.y,self.y,self.y,self.y,self.y,
        self.y,self.y,self.y,self.y,self.y,self.y,self.y,self.y,
        self.y,self.y,self.y,self.y,self.y,self.y,self.y,self.y,
        self.y,self.y,self.y,self.y,self.y,self.y,self.y,self.y,
        self.y,self.y,self.y,self.y,self.y,self.y,self.y,self.y
        ]
        self.sense.set_pixels(self.image)

    def eyes(self):
        self.sense.set_pixel(1,1,self.w)
        self.sense.set_pixel(1,2,self.w)
        self.sense.set_pixel(2,1,self.w)
        self.sense.set_pixel(2,2,self.b)
        self.sense.set_pixel(1,5,self.w)
        self.sense.set_pixel(1,6,self.w)
        self.sense.set_pixel(2,5,self.w)
        self.sense.set_pixel(2,6,self.b)
        
    def smile(self):
        self.sense.set_pixel(4,1,self.r)
        self.sense.set_pixel(4,2,self.r)
        self.sense.set_pixel(4,3,self.r)
        self.sense.set_pixel(4,4,self.r)
        self.sense.set_pixel(4,5,self.r)
        self.sense.set_pixel(4,6,self.r)
        self.sense.set_pixel(5,2,self.r)
        self.sense.set_pixel(5,3,self.b)
        self.sense.set_pixel(5,4,self.b)
        self.sense.set_pixel(5,5,self.r)
        self.sense.set_pixel(6,3,self.r)
        self.sense.set_pixel(6,4,self.r)
        
    def sad(self):
        self.sense.set_pixel(6,1,self.r)
        self.sense.set_pixel(5,2,self.r)
        self.sense.set_pixel(4,3,self.r)
        self.sense.set_pixel(4,4,self.r)
        self.sense.set_pixel(5,5,self.r)
        self.sense.set_pixel(6,6,self.r)
        
    def haww(self):
        self.sense.set_pixel(4,3,self.r)
        self.sense.set_pixel(4,4,self.r)
        self.sense.set_pixel(5,5,self.r)
        self.sense.set_pixel(6,4,self.r)
        self.sense.set_pixel(6,3,self.r)
        self.sense.set_pixel(5,2,self.r)
        self.sense.set_pixel(5,3,self.b)
        self.sense.set_pixel(5,4,self.b)
        

while True:
    s1 = Smiley()
    s1.eyes()
    s1.smile()
    sleep(3)
    s2 = Smiley()
    s2.eyes()
    s2.sad()
    sleep(3)
    s3 = Smiley()
    s3.eyes()
    s3.haww()
    sleep(3) 
    

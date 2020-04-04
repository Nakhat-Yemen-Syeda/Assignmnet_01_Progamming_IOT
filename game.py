from sense_hat import SenseHat
import time
import random
import csv
import datetime

class Dice:
    
    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()
        self.b = [0, 0, 0]
        self.r = [255, 0, 0]



    def roll_dice(self):
        self.sense.clear()
        r = random.randint(1,6)
        if r == 1:
            self.sense.set_pixel(3,3,self.r)
            self.sense.set_pixel(3,4,self.r)
            self.sense.set_pixel(4,3,self.r)
            self.sense.set_pixel(4,4,self.r)
        elif r == 2:
            self.sense.set_pixel(1,3,self.r)
            self.sense.set_pixel(1,4,self.r)
            self.sense.set_pixel(2,3,self.r)
            self.sense.set_pixel(2,4,self.r)
            self.sense.set_pixel(5,3,self.r)
            self.sense.set_pixel(5,4,self.r)
            self.sense.set_pixel(6,3,self.r)
            self.sense.set_pixel(6,4,self.r)
        elif r == 3:
            self.sense.set_pixel(1,3,self.r)
            self.sense.set_pixel(1,4,self.r)
            self.sense.set_pixel(2,3,self.r)
            self.sense.set_pixel(2,4,self.r)
            self.sense.set_pixel(5,1,self.r)
            self.sense.set_pixel(5,2,self.r)
            self.sense.set_pixel(6,1,self.r)
            self.sense.set_pixel(6,2,self.r)
            self.sense.set_pixel(5,5,self.r)
            self.sense.set_pixel(5,6,self.r)
            self.sense.set_pixel(6,5,self.r)
            self.sense.set_pixel(6,6,self.r)
        elif r == 4:
            self.sense.set_pixel(1,3,self.r)
            self.sense.set_pixel(1,4,self.r)
            self.sense.set_pixel(2,3,self.r)
            self.sense.set_pixel(2,4,self.r)
            self.sense.set_pixel(5,3,self.r)
            self.sense.set_pixel(5,4,self.r)
            self.sense.set_pixel(6,3,self.r)
            self.sense.set_pixel(6,4,self.r)
            self.sense.set_pixel(3,1,self.r)
            self.sense.set_pixel(3,2,self.r)
            self.sense.set_pixel(4,1,self.r)
            self.sense.set_pixel(4,2,self.r)
            self.sense.set_pixel(3,5,self.r)
            self.sense.set_pixel(3,6,self.r)
            self.sense.set_pixel(4,5,self.r)
            self.sense.set_pixel(4,6,self.r)
        elif r == 5:
            self.sense.set_pixel(0,3,self.r)
            self.sense.set_pixel(0,4,self.r)
            self.sense.set_pixel(1,3,self.r)
            self.sense.set_pixel(1,4,self.r)
            self.sense.set_pixel(3,3,self.r)
            self.sense.set_pixel(3,4,self.r)
            self.sense.set_pixel(4,3,self.r)
            self.sense.set_pixel(4,4,self.r)
            self.sense.set_pixel(6,3,self.r)
            self.sense.set_pixel(6,4,self.r)
            self.sense.set_pixel(7,3,self.r)
            self.sense.set_pixel(7,4,self.r)
            self.sense.set_pixel(3,0,self.r)
            self.sense.set_pixel(3,1,self.r)
            self.sense.set_pixel(4,0,self.r)
            self.sense.set_pixel(4,1,self.r)
            self.sense.set_pixel(3,6,self.r)
            self.sense.set_pixel(3,7,self.r)
            self.sense.set_pixel(4,6,self.r)
            self.sense.set_pixel(4,7,self.r)
        elif r == 6:
            self.sense.set_pixel(0,1,self.r)
            self.sense.set_pixel(0,2,self.r)
            self.sense.set_pixel(1,1,self.r)
            self.sense.set_pixel(1,2,self.r)
            self.sense.set_pixel(3,1,self.r)
            self.sense.set_pixel(3,2,self.r)
            self.sense.set_pixel(4,1,self.r)
            self.sense.set_pixel(4,2,self.r)
            self.sense.set_pixel(6,1,self.r)
            self.sense.set_pixel(6,2,self.r)
            self.sense.set_pixel(7,1,self.r)
            self.sense.set_pixel(7,2,self.r)
            self.sense.set_pixel(0,5,self.r)
            self.sense.set_pixel(0,6,self.r)
            self.sense.set_pixel(1,5,self.r)
            self.sense.set_pixel(1,6,self.r)
            self.sense.set_pixel(3,5,self.r)
            self.sense.set_pixel(3,6,self.r)
            self.sense.set_pixel(4,5,self.r)
            self.sense.set_pixel(4,6,self.r)
            self.sense.set_pixel(6,5,self.r)
            self.sense.set_pixel(6,6,self.r)
            self.sense.set_pixel(7,5,self.r)
            self.sense.set_pixel(7,6,self.r)
            
        return r
"""            
dice = Dice()
dice.sense.show_message("Shake")
        
while True:
    x, y, z = dice.sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)
   
    if x > 1.5 or y > 1.5 or z > 1.5:
        dice.roll_dice()
        
        """
        
        
        


class User:
    
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def addScore(self, num):
        self.score+=num
        

class Game:
    
    u1 = User("player 1")
    u2 = User("player 2")
    hat = SenseHat()
    
    message = "The players willshake Pi several times one by one until one player gets above 30 points. The player who gets above 30 points first is the winner."
    hat.show_message(message)
    
    d = Dice()
    
    while True:
    
        message = "P 1's turn :" + str(u1.score)
        hat.clear()
        hat.show_message(message)
        
        
        while True:
            x, y, z = hat.get_accelerometer_raw().values()
            x = abs(x)
            y = abs(y)
            z = abs(z)
            if x > 1.5 or y > 1.5 or z > 1.5:
                num = d.roll_dice()
                u1.addScore(num)
                time.sleep(2)
                break
        
        if (u1.score>=30):
            break
        
        message = "P 2's turn :" + str(u2.score)
        
        hat.clear()
        hat.show_message(message)
        
        while True:
            x, y, z = hat.get_accelerometer_raw().values()
            x = abs(x)
            y = abs(y)
            z = abs(z)
            
            if x > 1.5 or y > 1.5 or z > 1.5:
                num = d.roll_dice()
                u2.addScore(num)
                time.sleep(2)
                break;
        
        if (u2.score>=30):
            break
        
    curTime = datetime.datetime.now()
    curTime = (str(curTime))
    f = open("winners.csv", "a")
    
    if (u1.score>u2.score):
        hat.show_message("Player 1 wins")
        f.write(curTime + "," + " Player 1" + ", " + str(u1.score) + ", " + str(u2.score) + "\n")
        f.close()
        
        
    elif (u2.score>u1.score):
        hat.show_message("player 2 wins")
        f.write(curTime + "," + " Player 2" + ", " + str(u1.score) + ", " + str(u2.score) +"\n")
        f.close()
        
    else:
        hat.show_message("its a draw")
        f.write(curTime + "," + " Draw match" + ", " + str(u1.score) + ", " + str(u2.score) + "\n")
        f.close()

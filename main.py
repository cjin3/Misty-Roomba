from mistyPy.Robot import Robot
import time

misty = Robot()

currentTime = time.time()
timeRun = 3 #time program will run in seconds

LIN_SPEED = 30 
ANG_SPEED = 30

while(time.time()-currentTime < timeRun):
    if (canMoveForward):
        misty.move(speed, 0);

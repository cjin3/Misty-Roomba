from mistyPy.Robot import Robot
import time

misty = Robot()

currentTime = time.time()
timeRun = 3 #time program will run in seconds

LIN_SPEED = 30 #linear speed
ANG_SPEED = 30 #angular speed

def main():
    run = input("-1 for testing, 0 for autonomous, 1 for shared control")
    assert(run.isdigit()) 
    if int(run) == 0:
        autonomous()
    elif int(run) == -1:
        test()
    elif int(run) == 1:
        sharedControl()
    return 0
    


def autonomous():
    while(time.time()-currentTime < timeRun):
        if (canMoveForward()):
            misty.move(LIN_SPEED, 0)
        else:
            turn();

def canMoveForward():
    return 

main()
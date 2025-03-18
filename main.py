from mistyPy.Robot import Robot
from mistyPy.Events import Events
import time

''' 
Autonomous mode outline:

When running -> move forward

While item sensed -> turn left/right 
-Need to decide left or right so map can be designed
-Need to decide if multiple sensors need to detect item or just one

When robot reaches end of maze -> robot stops
-Need to decide how robot determines that they have gotten out of the maze
-Easiest way would be to have a counter for the number of turns the robot need to make (draw out a map perhaps)



Shared control outline:

When running -> move control

While item sensed -> relinquish control to human for turn
-What functions should be used for the robot go to the control interface?
-Once path forward is again detected, control goes back to robot
-How should we do this? Maybe some kind of delay

When robot reaches end of maze -> robot stops
-Same questions as the end step in autonomous mode
-Since robot doesn't make the turns this time, maybe the counter is the number of times the robot has to stop due to obstacle
'''
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
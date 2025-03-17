from mistyPy.GenerateRobot import RobotGenerator
RobotGenerator("ROBOT-IP_ADDRESS-GOES-HERE")

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

from robot import Robot
from robotNG import RobotNG

"""first_robot = Robot('Johnny 5')
first_robot.state()

first_robot.forward()
first_robot.turn_right()
first_robot.forward()
first_robot.forward()
first_robot.forward()

first_robot.state()

first_robot.turn_right()
first_robot.forward()
first_robot.state()

first_robot.turn_right()
first_robot.forward()
first_robot.state()

first_robot.turn_right()
first_robot.state()"""

new_robot = RobotNG('Terminator')
new_robot.state()
new_robot.forward(1)
new_robot.state()
new_robot.turn_right()
new_robot.state()
new_robot.boost()
new_robot.forward(1)
new_robot.state()
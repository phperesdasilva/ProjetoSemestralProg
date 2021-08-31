from robArm import robArm
from robGUI import showScreen
from pyfirmata import Arduino, SERVO 

board = Arduino('COM1')

robo = robArm(3, 9, 10, 11, board)

gui = showScreen(robo)

gui.runGUI()
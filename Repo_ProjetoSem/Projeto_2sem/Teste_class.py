from pyfirmata import SERVO, Arduino

from robArm import robArm
from robGUI import showScreen

board = Arduino('COM6')

robo = robArm(3, 9, 10, 11, board)

gui = showScreen(robo)

gui.runGUI()

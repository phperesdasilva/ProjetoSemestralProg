import PySimpleGUI as sg
from pyfirmata import Arduino, SERVO 
from time import sleep

port = 'COM6'
garra = 3
base = 9
x = 10
y = 11

board=Arduino(port)

board.digital[garra].mode = SERVO 
board.digital[base].mode = SERVO 
board.digital[x].mode = SERVO 
board.digital[y].mode = SERVO 

def rotateServo(pin1, pin2, pin3, pin4, prev, angle):
    if(angle<prev):
        t=-1
    elif(angle==prev):
        if prev>0:
            prev = prev-1
            t = 1
        else:
            prev = prev+1
            t=1
    else:
        t=1
    for i in range (prev, angle, t):   
        board.digital[pin1].write(i)
        board.digital[pin2].write(i)
        board.digital[pin3].write(i)
        board.digital[pin4].write(i)
        print(i)
        sleep(0.03)

#MÉTODO INEFICAZ DE SEGURANÇA
# def segurança():
#     rotateServo(x, 90, 90)
#     rotateServo(y, 50, 50)

# prevGarra = 90
# prevBase = 0

# rotateServo(garra, 90, 90)
# rotateServo(base, 100, 100)
# segurança()

while True:

    # segurança()
    # rotateServo(garra, prevGarra, 180)
    # rotateServo(base, prevBase, 180)
    # sleep(0.5)
    # rotateServo(garra, 180, prevGarra)
    # rotateServo(base, 180, prevBase)
    # sleep(0.5)
    rotateServo(garra, base, x, y, 50, 90)
    rotateServo(garra, base, x, y, 90, 50)
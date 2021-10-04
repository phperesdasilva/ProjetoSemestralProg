from pyfirmata import Arduino, SERVO 
from time import sleep
from tkinter import *

port = 'COM4'
pin1 = 3
pin2 = 9
pin3 = 10
pin4 = 11

board=Arduino(port)

board.digital[pin1].mode = SERVO 
board.digital[pin2].mode = SERVO 
board.digital[pin3].mode = SERVO 
board.digital[pin4].mode = SERVO 

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

root = Tk()
root.title('Tkinter Test')
root.geometry('400x400')

def getPos1(var):
    rotateServo(pin1, horizontal1.get())

def getPos2(var):
    rotateServo(pin2, horizontal2.get())

def getPos3(var):
    rotateServo(pin3, horizontal3.get())

def getPos4(var):
    rotateServo(pin4, horizontal4.get())

rotateServo(pin1, 90)
rotateServo(pin2, 0)
rotateServo(pin3, 90)
rotateServo(pin4, 90)

# horizontal1 = Scale(root, from_= 0, to=180, orient=HORIZONTAL, command=getPos1)
# horizonta1.grid(row=0, column=0)


# btn1 = Button(root, text='Pos. 1', command=getPos).grid(row=0, column=1)

root.mainloop()
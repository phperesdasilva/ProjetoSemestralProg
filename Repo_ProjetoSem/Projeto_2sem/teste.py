from pyfirmata import Arduino, SERVO 
from time import sleep
from tkinter import *

port = 'COM4'
pin = 11

board=Arduino(port)

board.digital[pin].mode = SERVO 

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

root = Tk()
root.title('Tkinter Test')
root.geometry('400x400')

def getPos(var):
    rotateServo(pin, horizontal.get())

horizontal = Scale(root, from_= 0, to=180, orient=HORIZONTAL, command=getPos)
horizontal.grid(row=0, column=0)

# btn1 = Button(root, text='Pos. 1', command=getPos).grid(row=0, column=1)

root.mainloop()
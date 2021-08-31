import PySimpleGUI as sg
from pyfirmata import Arduino, SERVO 
from time import sleep

class robArm:
    def __init__(self, garra, base, eixoX, eixoY, board):
        self.garra = garra
        self.base = base
        self.eixoX = eixoX
        self.eixoY = eixoY
        self.board = board

        self.board.digital[garra].mode = SERVO 
        self.board.digital[base].mode = SERVO 
        self.board.digital[eixoX].mode = SERVO 
        self.board.digital[eixoY].mode = SERVO 

    def sendPos(self, pin, prev, angle, spd):
        i = prev
        if(angle<prev):
            while(i>angle):
                self.board.digital[pin].write(i)
                i = i - 1
                sleep(spd)
        elif(angle>prev):
            while(i<angle):
                i = i + 1
                self.board.digital[pin].write(i)
                sleep(spd)                
        elif(angle==prev):
            self.board.digital[pin].write(i)
            sleep(spd)
    
    def runPos(self, lista, speed):
        for i in range (5):
            if(i!=0):
                self.sendPos(garra, lista[i-1][0], lista[i][0], speed)
                self.sendPos(base, lista[i-1][1], lista[i][1], speed)
                self.sendPos(eixoX, lista[i-1][2], lista[i][2], speed)
                self.sendPos(eixoY, lista[i-1][3], lista[i][3], speed)
                sleep(0.25)
            else:
                self.sendPos(garra, lista[i][0], lista[i][0], speed)
                self.sendPos(base, lista[i][1], lista[i][1], speed)
                self.sendPos(eixoX, lista[i][2], lista[i][2], speed)
                self.sendPos(eixoY, lista[i][3], lista[i][3], speed)
                sleep(0.25)

    def segurança(self):
        self.sendPos(garra, 180, 180, 0.06)
        self.sendPos(base, 100, 100, 0.06)
        self.sendPos(eixoX, 90, 90, 0.06)
        self.sendPos(eixoY, 50, 50, 0.06)


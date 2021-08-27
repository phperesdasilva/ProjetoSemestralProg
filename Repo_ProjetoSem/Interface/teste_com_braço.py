import PySimpleGUI as sg
from pyfirmata import Arduino, SERVO 
from time import sleep
from tkinter import *

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

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

#MÉTODO INEFICAZ DE SEGURANÇA
def segurança():
    rotateServo(garra, 180)
    rotateServo(base, 100)
    rotateServo(x, 90)
    rotateServo(y, 50)

segurança()

def menu():
    layout = [
        [sg.Text('inserir título')],
        [sg.Button('Função livre', size=(20,5))],
        [sg.Button('Função 2', size=(20,5))]

    ]

    return sg.Window('menu', layout=layout, finalize=True)

def func1():
    layout = [
        [sg.Text('Garra'), sg.Slider(range=(90,180), default_value=180, size=(20,15), orientation='horizontal', key='garra', change_submits=True, font=('Helvetica', 12))],
        [sg.Text('Base'), sg.Slider(range=(0,180), default_value=100, size=(20,15), orientation='horizontal', key='base', change_submits=True, font=('Helvetica', 12))],
        [sg.Text('Eixo X'), sg.Slider(range=(0,180), default_value=90, size=(20,15), orientation='horizontal', key='x', change_submits=True, font=('Helvetica', 12))],
        [sg.Text('Eixo Y'), sg.Slider(range=(0,108), default_value=50, size=(20,15), orientation='horizontal', key='y', change_submits=True, font=('Helvetica', 12))],
        [sg.Button('Pos. 1'), sg.Button('Pos. 2'), sg.Button('Pos. 3'), sg.Button('Pos. 4'), sg.Button('Pos. 5')],
        [sg.Button('Run', button_color='green'), sg.Button('Clear', button_color='red')],
        [sg.Button('voltar')]

    ]

    return sg.Window('Função Livre', layout=layout, finalize=True)

def func2():
    layout = [
        [sg.Text('TBD')],
        [sg.Button('voltar')]

    ]

    return sg.Window('função 2', layout=layout, finalize=True)

def mandarPos(win, ev, servo):
    if window == win and event == ev:
        rotateServo(servo, values[0])

def lerPos(win, ev, lista):
    if window == win and event == ev:
        if len(lista) != 4:
            lista.append(values['garra'])
            lista.append(values['base'])
            lista.append(values['x'])
            lista.append(values['y'])
            sg.Popup('Nova posição!:', 'Garra: '+ str(lista[0]), 'Base: '+ str(lista[1]), 'Eixo X: '+ str(lista[2]), 'Eixo Y: '+ str(lista[3]))
        else:
            sg.Popup('Coordenadas:', 'Garra: '+ str(lista[0]), 'Base: '+ str(lista[1]), 'Eixo X: '+ str(lista[2]), 'Eixo Y: '+ str(lista[3]))

def runPos(lista, delay):
    for i in range (5):
        rotateServo(garra, lista[i][0])
        rotateServo(base, lista[i][1])
        rotateServo(x, lista[i][2])
        rotateServo(y, lista[i][3])
        sleep(delay)

w1, w2 = menu(), None

pos = []
pos1 = []
pos2 = []
pos3 = []
pos4 = []
pos5 = []

pos.append(pos1)
pos.append(pos2)
pos.append(pos3)
pos.append(pos4)
pos.append(pos5)

while True:

    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        segurança()
        sleep(1)
        break


    if window == w1 and event == 'Função livre':
        segurança()
        w1.hide()
        w2 = func1()
    elif window == w1 and event == 'Função 2':
        segurança()
        w1.hide()
        w2 = func2()

    if event == 'voltar':
        segurança()
        w2.hide()
        w1.un_hide()

    if window == w2 and event == 'garra':
        rotateServo(garra, int(values['garra']))
    
    if window == w2 and event == 'base':
        rotateServo(base, int(values['base']))

    if window == w2 and event == 'x':
        rotateServo(x, int(values['x']))

    if window == w2 and event == 'y':
        rotateServo(y, int(values['y']))

    lerPos(w2, 'Pos. 1', pos1)
    lerPos(w2, 'Pos. 2', pos2)
    lerPos(w2, 'Pos. 3', pos3)
    lerPos(w2, 'Pos. 4', pos4)
    lerPos(w2, 'Pos. 5', pos5)

    # if window == w2 and event =='Pos. 1':
    #     if len(pos1) != 4:
    #         pos1.append(values[0])
    #         pos1.append(values[1])
    #         pos1.append(values[2])
    #         pos1.append(values[3])
    #         sg.Popup('Nova posição!:', 'Pos. R: '+ str(pos1[0]), 'Pos. X: '+ str(pos1[1]), 'Pos. Y: '+ str(pos1[2]), 'Pos. Z: '+ str(pos1[3]))
    #     else:
    #         sg.Popup('Coordenadas:', 'Pos. R: '+ str(pos1[0]), 'Pos. X: '+ str(pos1[1]), 'Pos. Y: '+ str(pos1[2]), 'Pos. Z: '+ str(pos1[3]))

    # if window == w2 and event =='Pos. 2':
    #     if len(pos2) != 4:
    #         pos2.append(values[0])
    #         pos2.append(values[1])
    #         pos2.append(values[2])
    #         pos2.append(values[3])
    #         sg.Popup('Nova posição!:', 'Pos. R: '+ str(pos2[0]), 'Pos. X: '+ str(pos2[1]), 'Pos. Y: '+ str(pos2[2]), 'Pos. Z: '+ str(pos2[3]))
    #     else:
    #         sg.Popup('Coordenadas:', 'Pos. R: '+ str(pos2[0]), 'Pos. X: '+ str(pos2[1]), 'Pos. Y: '+ str(pos2[2]), 'Pos. Z: '+ str(pos2[3]))


    # if window == w2 and event =='Pos. 3':
    #     if len(pos3) != 4:
    #         pos3.append(values[0])
    #         pos3.append(values[1])
    #         pos3.append(values[2])
    #         pos3.append(values[3])
    #         sg.Popup('Nova posição!:', 'Pos. R: '+ str(pos3[0]), 'Pos. X: '+ str(pos3[1]), 'Pos. Y: '+ str(pos3[2]), 'Pos. Z: '+ str(pos3[3]))
    #     else:
    #         sg.Popup('Coordenadas:', 'Pos. R: '+ str(pos3[0]), 'Pos. X: '+ str(pos3[1]), 'Pos. Y: '+ str(pos3[2]), 'Pos. Z: '+ str(pos3[3]))


    # if window == w2 and event =='Pos. 4':
    #     if len(pos4) != 4:
    #         pos4.append(values[0])
    #         pos4.append(values[1])
    #         pos4.append(values[2])
    #         pos4.append(values[3])
    #         sg.Popup('Nova posição!:', 'Pos. R: '+ str(pos4[0]), 'Pos. X: '+ str(pos4[1]), 'Pos. Y: '+ str(pos4[2]), 'Pos. Z: '+ str(pos4[3]))
    #     else:
    #         sg.Popup('Coordenadas:', 'Pos. R: '+ str(pos4[0]), 'Pos. X: '+ str(pos4[1]), 'Pos. Y: '+ str(pos4[2]), 'Pos. Z: '+ str(pos4[3]))

    # if window == w2 and event =='Pos. 5':
    #     if len(pos5) != 4:
    #         pos5.append(values[0])
    #         pos5.append(values[1])
    #         pos5.append(values[2])
    #         pos5.append(values[3])
    #         sg.Popup('Nova posição!:', 'Pos. R: '+ str(pos5[0]), 'Pos. X: '+ str(pos5[1]), 'Pos. Y: '+ str(pos5[2]), 'Pos. Z: '+ str(pos5[3]))
    #     else:
    #         sg.Popup('Coordenadas:', 'Pos. R: '+ str(pos5[0]), 'Pos. X: '+ str(pos5[1]), 'Pos. Y: '+ str(pos5[2]), 'Pos. Z: '+ str(pos5[3]))

    
    if window == w2 and event =='Clear':
        pos1.clear()
        pos2.clear()
        pos3.clear()
        pos4.clear()
        pos5.clear()
        sg.Popup('Posições zeradas!')


    if window == w2 and event =='Run':
        runPos(pos, 1.5)
        sg.Popup(':)')
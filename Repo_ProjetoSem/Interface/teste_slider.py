import PySimpleGUI as sg

def menu():
    layout = [
        [sg.Text('inserir título')],
        [sg.Button('Função livre', size=(20,5))],
        [sg.Button('Função 2', size=(20,5))]

    ]

    return sg.Window('menu', layout=layout, finalize=True)

def func1():
    layout = [
        [sg.Text('Pos. R'), sg.Slider(range=(0,100), default_value=0, size=(20,15), orientation='horizontal', font=('Helvetica', 12))],
        [sg.Text('Pos. X'), sg.Slider(range=(0,100), default_value=0, size=(20,15), orientation='horizontal', font=('Helvetica', 12))],
        [sg.Text('Pos. Y'), sg.Slider(range=(0,100), default_value=0, size=(20,15), orientation='horizontal', font=('Helvetica', 12))],
        [sg.Text('Pos. Z'), sg.Slider(range=(0,100), default_value=0, size=(20,15), orientation='horizontal', font=('Helvetica', 12))],
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

def lerPos(win, ev, lista):
    if window == win and event == ev:
        if len(lista) != 4:
            lista.append(values[0])
            lista.append(values[1])
            lista.append(values[2])
            lista.append(values[3])
            sg.Popup('Nova posição!:', 'Pos. R: '+ str(lista[0]), 'Pos. X: '+ str(lista[1]), 'Pos. Y: '+ str(lista[2]), 'Pos. Z: '+ str(lista[3]))
        else:
            sg.Popup('Coordenadas:', 'Pos. R: '+ str(lista[0]), 'Pos. X: '+ str(lista[1]), 'Pos. Y: '+ str(lista[2]), 'Pos. Z: '+ str(lista[3]))


w1, w2 = menu(), None

pos1 = []
pos2 = []
pos3 = []
pos4 = []
pos5 = []

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break
    
    if window == w1 and event == 'Função livre':
        w1.hide()
        w2 = func1()
    elif window == w1 and event == 'Função 2':
        w1.hide()
        w2 = func2()

    if event == 'voltar':
        w2.hide()
        w1.un_hide()
    
    lerPos(w2, 'Pos. 1', pos1)
    lerPos(w2, 'Pos. 2', pos2)
    lerPos(w2, 'Pos. 3', pos3)
    lerPos(w2, 'Pos. 4', pos4)
    lerPos(w2, 'Pos. 5', pos5)
    
    if window == w2 and event =='Clear':
        pos1.clear()
        pos2.clear()
        pos3.clear()
        pos4.clear()
        pos5.clear()
        sg.Popup('Posições zeradas!')


    if window == w2 and event =='Run':
        sg.Popup('TBD')
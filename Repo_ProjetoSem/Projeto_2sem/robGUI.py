from time import sleep
import PySimpleGUI as sg
from robArm import robArm

class showScreen:
    def __init__(self, robo):
        self.robo = robo
        self.window = None
        self.event = None
        self.values = None

    def menu(self):
        layout = [
        [sg.Text('Braço Robótico')],
        [sg.Button('Função livre', size=(10,3))],
        [sg.Button('Função 2', size=(10,3))]

        ]

        return sg.Window('menu', layout=layout, finalize=True)
    
    def func1(self):
        layout = [
            [sg.Text('Garra'), sg.Slider(range=(90,180), default_value=180, size=(20,15), orientation='horizontal', key='garra', change_submits=True, font=('Helvetica', 12))],
            [sg.Text('Base'), sg.Slider(range=(0,180), default_value=100, size=(20,15), orientation='horizontal', key='base', change_submits=True, font=('Helvetica', 12))],
            [sg.Text('Eixo X'), sg.Slider(range=(0,180), default_value=90, size=(20,15), orientation='horizontal', key='x', change_submits=True, font=('Helvetica', 12))],
            [sg.Text('Eixo Y'), sg.Slider(range=(0,180), default_value=50, size=(20,15), orientation='horizontal', key='y', change_submits=True, font=('Helvetica', 12))],
            #[sg.Text('Veloc.'), sg.Slider(range=(50,100), default_value=50, size=(20,15), orientation='horizontal', key='spd', change_submits=True, font=('Helvetica', 12))],
            [sg.Button('Pos. 1'), sg.Button('Pos. 2'), sg.Button('Pos. 3'), sg.Button('Pos. 4'), sg.Button('Pos. 5')],
            [sg.Button('Run', button_color='green'), sg.Button('Clear', button_color='red'), sg.Button('Reset Pos.')],
            [sg.Button('voltar')]

        ]

        return sg.Window('Função Livre', layout=layout, finalize=True)

    def func2(self):
        layout = [
            [sg.Text('TBD')],
            [sg.Button('voltar')]

        ]

        return sg.Window('função 2', layout=layout, finalize=True)

    def lerPos(self, win, ev, lista):
        if self.window == win and self.event == ev:
            if len(lista) != 4:
                lista.append(int(self.values['garra']))
                lista.append(int(self.values['base']))
                lista.append(int(self.values['x']))
                lista.append(int(self.values['y']))
                sg.Popup('Nova posição!:', 'Garra: '+ str(lista[0]), 'Base: '+ str(lista[1]), 'Eixo X: '+ str(lista[2]), 'Eixo Y: '+ str(lista[3]))
            else:
                sg.Popup('Coordenadas:', 'Garra: '+ str(lista[0]), 'Base: '+ str(lista[1]), 'Eixo X: '+ str(lista[2]), 'Eixo Y: '+ str(lista[3]))

    def rodaPos(self, win, ev, var, pin):
        if self.window == win and self.event == ev:
            self.robo.sendPos(pin, int(self.values[var]), int(self.values[var]), 0.06)

    def runGUI(self):

        self.robo.segurança()

        w1, w2 = self.menu(), None

        pos = [[], [], [], [], []]

        while True:

            self.window, self.event, self.values = sg.read_all_windows()

            if self.event == sg.WIN_CLOSED:
                self.robo.segurança()
                sleep(1)
                break


            if self.window == w1 and self.event == 'Função livre':
                self.robo.segurança()
                w1.hide()
                w2 = self.func1()
            elif self.window == w1 and self.event == 'Função 2':
                self.robo.segurança()
                w1.hide()
                w2 = self.func2()

            if self.event == 'voltar':
                self.robo.segurança()
                w2.hide()
                w1.un_hide()

            self.rodaPos(w2, 'garra', 'garra', self.robo.garra)
            self.rodaPos(w2, 'base', 'base', self.robo.base)
            self.rodaPos(w2, 'x', 'x', self.robo.eixoX)
            self.rodaPos(w2, 'y', 'y', self.robo.eixoY)
            
            self.lerPos(w2, 'Pos. 1', pos[0])
            self.lerPos(w2, 'Pos. 2', pos[1])
            self.lerPos(w2, 'Pos. 3', pos[2])
            self.lerPos(w2, 'Pos. 4', pos[3])
            self.lerPos(w2, 'Pos. 5', pos[4])

            if self.window == w2 and self.event =='Clear':
                pos[0].clear()
                pos[1].clear()
                pos[2].clear()
                pos[3].clear()
                pos[4].clear()
                sg.Popup('Posições zeradas!')


            if self.window == w2 and self.event =='Run':
                self.robo.runPos(pos, 0.03)
                sg.Popup(':)')

            if self.window == w2 and self.event =='Reset Pos.':
                self.robo.segurança()
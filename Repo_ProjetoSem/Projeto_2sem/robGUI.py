from time import sleep

import PySimpleGUI as sg

from robArm import robArm

class showScreen:
    sg.theme('LightGray6')

    def __init__(self, robo):
        self.robo = robo
        self.window = None
        self.event = None
        self.values = None
        
        self.bg_size = (800,400)
        self.gif = 'C:/Users/First Place/Documents/GitHub/ProjetoSemestralProg/Images/gif garra.gif'

    def menu(self):
        layout = [
        [sg.Text('Interface - Braço Robótico', size=(20,0), font=('Times 25 bold'), justification='c')],
        [sg.Image(filename=self.gif, key='gif')],
        [sg.Button('Função Livre', size=(10,2)), sg.Button('Função Cópia', size=(10,2)), sg.Button('Help', size=(3,1))]
        ]

        return sg.Window('Interface - Braço Robótico', grab_anywhere=False, size=self.bg_size, transparent_color=None, layout=layout, no_titlebar=False, element_justification='c', finalize=True)
    
    def guide(self):
        layout = [
            [sg.Text('Função Livre:', font=('Times 14'))],
            [sg.Text('- Possui sliders para movimentar cada servo do robô individualmente.')],
            [sg.Text('- Cada botão memoriza as posições dos servos.')],
            [sg.Text('- Uma vez gravada as posições, clicar novamente no botão irá exibir as coordenadas memorizadas.')],
            [sg.Text('- O botão "Reset Pos." limpa a memória.')],
            [sg.Text('- O botão "Idle Pos." retorna o robô para sua posição de espera.')],
            [sg.Text('- O botão "Run" faz com que o robô passe pelas coordenadas em ordem de posição.')],
            [sg.Text('Função Cópia:', font=('Times 14'))],
            [sg.Text('- O robô posicionador deve ser movido para a posição desejada.')],
            [sg.Text('- A posição do robô posicionador será exibida no gráfico ao lado.')],
            [sg.Text('- Cada botão memoriza as posições dos servos.')],
            [sg.Text('- Uma vez gravada as posições, clicar novamente no botão irá exibir as coordenadas memorizadas.')],
            [sg.Text('- O botão "Reset Pos." limpa a memória.')],
            [sg.Text('- O botão "Idle Pos." retorna o robô para sua posição de espera.')],
            [sg.Text('- O botão "Run" faz com que o robô passe pelas coordenadas em ordem de posição.')]
        ]

        return sg.Window('Help', icon=self.gif, element_justification='l', layout=layout, finalize=True)
    
    def func1(self):
        layout = [
            [sg.Text('Garra'), sg.Slider(range=(90,180), default_value=180, size=(40,15), orientation='horizontal', key='garra', change_submits=True, font=('Helvetica', 12))],
            [sg.Text('Base'), sg.Slider(range=(0,180), default_value=100, size=(40,15), orientation='horizontal', key='base', change_submits=True, font=('Helvetica', 12))],
            [sg.Text('Eixo X'), sg.Slider(range=(0,180), default_value=90, size=(40,15), orientation='horizontal', key='x', change_submits=True, font=('Helvetica', 12))],
            [sg.Text('Eixo Y'), sg.Slider(range=(0,180), default_value=50, size=(40,15),  orientation='horizontal', key='y', change_submits=True, font=('Helvetica', 12))],
            [sg.Button('Pos. 1', size=(10,2)), sg.Button('Pos. 2', size=(10,2)), sg.Button('Pos. 3', size=(10,2)), sg.Button('Pos. 4', size=(10,2)), sg.Button('Pos. 5', size=(10,2))],
            [sg.Button('Run', button_color='green'), sg.Button('Clear', button_color='red'), sg.Button('Reset Pos.'), sg.Button('Idle Pos.')],
            [sg.Button('Voltar')], 
            [sg.Button('Help', pad=(100,0))]

        ]

        return sg.Window('Função Livre', icon=self.gif, element_justification='c', layout=layout, size=self.bg_size, finalize=True)

    def func2(self):
        options = [
            [sg.Button('Pos. 1', size=(10,2))],
            [sg.Button('Pos. 2', size=(10,2))], 
            [sg.Button('Pos. 3', size=(10,2))], 
            [sg.Button('Pos. 4', size=(10,2))], 
            [sg.Button('Pos. 5', size=(10,2))],
            [sg.Button('Reset Pos.')],
            [sg.Button('Idle Pos.')],
            [sg.Button('Run', button_color='green'), sg.Button('Clear', button_color='red')], 
            [sg.Button('Voltar'), sg.Button('Help', pad=(100,0))]
        ]

        layout = [
            [
                sg.Graph(
                    canvas_size=(300, 380),
                    graph_bottom_left=(0, 0),
                    graph_top_right=(800, 800),
                    key="grafico",
                    enable_events=True,
                    background_color="white",
                    drag_submits=True,
                    
                ),
                sg.Col(options),
            ]
        ]

        return sg.Window('Função Cópia', icon=self.gif, element_justification='c', size=self.bg_size, layout=layout, finalize=True)

    def lerPos(self, win, ev, lista):
        if self.window == win and self.event == ev:
            if len(lista) != 4:
                print('lista antes')
                print(self.values)
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

            if self.window == w1 and self.event == 'Função Livre':
                self.robo.segurança()
                w1.hide()
                w2 = self.func1()
                tela = 1
            elif self.window == w1 and self.event == 'Função Cópia':
                self.robo.segurança()
                w1.hide()
                w2 = self.func2()
                tela = 2

            if self.event == 'Help':
                sg.Popup("""Função Livre:

- Possui sliders para movimentar cada servo do robô individualmente.
- Cada botão memoriza as posições dos servos.
- Uma vez gravada as posições, clicar novamente no botão irá exibir as coordenadas memorizadas.
- O botão "Reset Pos." limpa a memória.
- O botão "Idle Pos." retorna o robô para sua posição de espera.
- O botão "Run" faz com que o robô passe pelas coordenadas em ordem de posição.

Função Cópia:

- O robô posicionador deve ser movido para a posição desejada.
- A posição do robô posicionador será exibida no gráfico ao lado.
- Cada botão memoriza as posições dos servos.
- Uma vez gravada as posições, clicar novamente no botão irá exibir as coordenadas memorizadas.
- O botão "Reset Pos." limpa a memória.
- O botão "Idle Pos." retorna o robô para sua posição de espera.
- O botão "Run" faz com que o robô passe pelas coordenadas em ordem de posição.""")

            if self.event == 'Voltar':
                self.robo.segurança()
                pos[0].clear()
                pos[1].clear()
                pos[2].clear()
                pos[3].clear()
                pos[4].clear()
                w2.hide()
                w1.un_hide()

            if self.window == w2 and tela == 1:
                self.rodaPos(w2, 'garra', 'garra', self.robo.garra)
                self.rodaPos(w2, 'base', 'base', self.robo.base)
                self.rodaPos(w2, 'x', 'x', self.robo.eixoX)
                self.rodaPos(w2, 'y', 'y', self.robo.eixoY)
                
                self.lerPos(w2, 'Pos. 1', pos[0])
                self.lerPos(w2, 'Pos. 2', pos[1])
                self.lerPos(w2, 'Pos. 3', pos[2])
                self.lerPos(w2, 'Pos. 4', pos[3])
                self.lerPos(w2, 'Pos. 5', pos[4])

            if self.event =='Clear':
                pos[0].clear()
                pos[1].clear()
                pos[2].clear()
                pos[3].clear()
                pos[4].clear()
                sg.Popup('Posições zeradas!')


            if self.event =='Run':
                self.robo.runPos(pos, 0.03)
                sg.Popup(':)')

            if self.event =='Idle Pos.':
                self.robo.segurança()
import PySimpleGUI as sg

#func. janelas
def login():
    sg.theme('DarkAmber')
    layout =[
        [sg.Text('nome')],
        [sg.Input()],
        [sg.Button('continuar')]
    ]

    return sg.Window('login', layout=layout, finalize=True)

def pedido():
    sg.theme('DarkAmber')
    layout =[
        [sg.Text('fazer pedido')],
        [sg.Checkbox('Pizza 1', key='pizza1'), sg.Checkbox('Pizza 2', key='pizza2')],
        [sg.Button('voltar'), sg.Button('fazer pedido')]
    ]
    return sg.Window('pedido', layout=layout, finalize=True)

#janelas iniciais
janela1, janela2 = login(), None

#criar loop de leitura
while True:
    window, event, values = sg.read_all_windows()
    #janela fechada
    if event == sg.WIN_CLOSED:
        break
    #proxima janela
    if window == janela1 and event == 'continuar':
        janela2 = pedido()
        janela1.hide()

    #voltar
    if window == janela2 and event == 'voltar':
        janela2.hide()
        janela1.un_hide()

    #pedido
    if window == janela2 and event == 'fazer pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('foram pedidas ambas as pizzas')
        elif values['pizza1'] == True:
            sg.popup('foi pedida a pizza 1')
        elif values['pizza2'] == True:
            sg.popup('foi pedida a pizza 2')
        
import PySimpleGUI as sg      

layout = [      
            [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0,0), graph_top_right=(400, 400), background_color='white', key='graph')],      
            [sg.Text('Eixo X'), sg.Slider(range=(0,400), default_value=50, size=(20,15), orientation='horizontal', key='x', change_submits=True, font=('Helvetica', 12))],
            [sg.Text('Eixo Y'), sg.Slider(range=(0,400), default_value=50, size=(20,15), orientation='horizontal', key='y', change_submits=True, font=('Helvetica', 12))],
            [sg.T('Change circle color to:'), sg.Button('Red'), sg.Button('Blue'), sg.Button('Move')]      
            ]      

window = sg.Window('Graph test', layout, finalize=True)       

graph = window['graph']  
circle = graph.DrawCircle((200,200), 25, fill_color='black',line_color='white')      
point = graph.DrawPoint((75,75), 10, color='green')      
oval = graph.DrawOval((25,300), (100,280), fill_color='purple', line_color='purple'  )      
rectangle = graph.DrawRectangle((25,300), (100,280), line_color='purple'  )      
line = graph.DrawLine((0,0), (100,100))      

while True:      
    event, values = window.read()      
    if event == sg.WIN_CLOSED:      
        break      
    if event is 'Blue':      
        graph.TKCanvas.itemconfig(circle, fill = "Blue")      
    elif event is 'Red':      
        graph.TKCanvas.itemconfig(circle, fill = "Red")      
    elif event is 'x' or 'y':      
        graph.update(point, int(values['x']), int(values['y']))      
        # graph.MoveFigure(circle, int(values['x']), int(values['y']))      
        # graph.MoveFigure(oval, int(values['x']), int(values['y']))      
        # graph.MoveFigure(rectangle, int(values['x']), int(values['y']))      
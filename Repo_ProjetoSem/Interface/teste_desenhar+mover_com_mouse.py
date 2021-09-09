import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Graph

options = [
    [sg.R("desenhar circulo", 1, key="circ", enable_events=True)],
    [sg.R("mover", 1, key="mov", enable_events=True)],
]

layout = [
    [
        sg.Graph(
            canvas_size=(400, 400),
            graph_bottom_left=(0, 0),
            graph_top_right=(800, 800),
            key="grafico",
            enable_events=True,
            background_color="lightblue",
            drag_submits=True,
            right_click_menu=[
                [],
                [
                    "Erase item",
                ],
            ],
        ),
        sg.Col(options, key="op"),
    ]
]

window = sg.Window("teste desenhar e mexer", layout, finalize=True)

grafico = window["grafico"]

dragging = False
start_point = end_point = prior_rect = None

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "mov":
        grafico.set_cursor(cursor="fleur")

    if event == "grafico":  # if there's a "Graph" event, then it's a mouse
        x, y = values["grafico"]
        if not dragging:
            start_point = (x, y)
            dragging = True
            drag_figures = grafico.get_figures_at_location((x, y))
            lastxy = x, y
        else:
            end_point = (x, y)
        if prior_rect:
            grafico.delete_figure(prior_rect)
        delta_x, delta_y = x - lastxy[0], y - lastxy[1]
        lastxy = x, y
        if None not in (start_point, end_point):
            if values["mov"]:
                for fig in drag_figures:
                    grafico.move_figure(fig, delta_x, delta_y)
                    grafico.update()
            elif values["circ"]:
                prior_rect = grafico.draw_circle(
                    start_point,
                    end_point[0] - start_point[0],
                    fill_color="red",
                    line_color="green",
                )
    elif event.endswith("+UP"):  # The drawing has ended because mouse up
        start_point, end_point = None, None  # enable grabbing a new rect
        dragging = False
        prior_rect = None

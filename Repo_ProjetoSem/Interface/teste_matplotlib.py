import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PySimpleGUI as sg



# set up the figure and subplot
fig = plt.figure()
fig.canvas.set_window_title('Matplotlib Animation')
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-2,6))
ax.grid()
ax.set_title('Piston Motion Animation')
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
line, = ax.plot([], [], 'o-', lw=5, color='#de2d26')


# initialization function
def init():
    line.set_data([], [])
    return line,

# animation function
def animate(i):
    x_points = [0, x1, x2]
    y_points = [0, 10, x1]

    line.set_data(x_points, y_points)
    return line,

# call the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=120, interval=40, blit=True, repeat=False)
## to save animation, uncomment the line below:
## ani.save('offset_piston_motion_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#show the animation
plt.show()

layout = [
    [sg.Slider(range=(1,180), key='x1', change_submits=True, size=(20,10), orientation='horizontal')],
    [sg.Slider(range=(1,180), key='x2', change_submits=True, size=(20,10), orientation='horizontal')]
]

window = sg.Window('teste', layout, finalize=True)

while True:

    event, values = window.read()

    fig = plt.figure()
    fig.canvas.set_window_title('Matplotlib Animation')
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-2,6))
    ax.grid()
    ax.set_title('Piston Motion Animation')
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    line, = ax.plot([], [], 'o-', lw=5, color='#de2d26')


    # initialization function
    def init():
        line.set_data([], [])
        return line,

    # animation function
    def animate(x1, x2):
        x_points = [0, x1, x2]
        y_points = [0, 10, x1]

        line.set_data(x_points, y_points)
        return line,

    # call the animation
    ani = animation.FuncAnimation(fig, animate(values['x1'], values['x2']), init_func=init, frames=120, interval=40, blit=True, repeat=False)
    ## to save animation, uncomment the line below:
    ## ani.save('offset_piston_motion_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

    #show the animation
    plt.show()
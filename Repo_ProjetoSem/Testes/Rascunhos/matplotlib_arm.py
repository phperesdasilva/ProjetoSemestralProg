#Written by Travis DeWolf (Sept, 2013)
#Based on code by Jake Vanderplas - http://jakevdp.github.com
 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import PySimpleGUI as sg

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-1, 1), ylim=(-1, 1))
ax.grid()
 
line = ax.plot([], [], 'o-', lw=4, mew=5)

def animate(x,y):
    line.set_data(x,y)
    return line

ani = animation.FuncAnimation(fig, animate(x, y), frames=None,
                              interval=25, blit=True, 
                              init_func=line.set_data([],[]))

plt.show()
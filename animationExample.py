import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#set up the figure
fig = plt.figure()
ax = plt.subplot(111, projection = 'polar')
line, = ax.plot([], [], lw = 2)
ax.set_rmax(2.0)

#define theta
theta = np.linspace(0, 2 * np.pi,  1024)

#init function for background drawing every frame
def init():
    line.set_data([], [])
    return line,

#animation funciton, called in every frame
def animate(i):
    r = np.cos(0.01 * theta * i)
    line.set_data(theta, r)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 25,  blit = False)

plt.show()

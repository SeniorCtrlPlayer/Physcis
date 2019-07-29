import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    # x_out = [r_out*np.cos(theta[i]) for i in range(len(theta))]
    x_out = r_out * np.cos(theta)
    y_out = r_out * np.sin(theta)
    ln1.set_data(x_out, y_out)
    return ln1,

def update(i):
    x_in = [(r_out-r_in)*np.cos(theta[i])+r_in*np.cos(theta[j]) for j in range(len(theta))]
    y_in = [(r_out-r_in)*np.sin(theta[i])+r_in*np.sin(theta[j]) for j in range(len(theta))]
    ln2.set_data(x_in, y_in)
    return ln2,

def gen_dot():
    for i in theta:
        yield i

def update_p(theta):
    r = r_out * 0.8
    dot.set_data(r * np.cos(theta), r * np.sin(theta))
    return dot,

def update_line(theta):
    x = H * r * np.cos(theta) / (h + r * np.sin(theta))
    y = 1.5
    line_x = np.zeros(3)
    line_y = np.zeros(3)
    line_x[1] = x
    line_y[0] = -2
    line_y[1] = y
    line_x[2] = x + 1
    line_y[2] = y
    ln2.set_data(line_x, line_y)
    # ln2.set_data(1, 1)
    # dot1 = update(theta)
    dot.set_data(r * np.cos(theta), r * np.sin(theta))

    return ln2, dot

if __name__ == '__main__':

    fig = plt.figure(figsize=(6, 6))
    ax = plt.gca()
    ax.grid()
    ln1, = ax.plot([], [], '-', lw=2)
    ln2, = ax.plot([], [], '-', color='r', lw=2)
    dot, = ax.plot([], [], 'ro')

    ani = animation.FuncAnimation(fig, update_line, frames=gen_dot, init_func=init, interval=5)

    plt.show()
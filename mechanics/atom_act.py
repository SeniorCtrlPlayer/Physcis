import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# import random
import math


def func_get_prime(n):
    return list(filter(lambda x: not [x % i for i in range(2, int(math.sqrt(x)) + 1) if x % i == 0],
                  range(2, n + 1)))

def init():
    """
    设置输出坐标轴
    :return:
    """
    ax.set_xlim(0, np.mean(atoms)*100)
    ax.set_ylim(0, len(energy)+1)
    # x_out = [r_out*np.cos(theta[i]) for i in range(len(theta))]

    return ln1,

# def gen_time():
#     for i in range(10):
#         yield i


def update_p(i):
    """
    更新各粒子坐标和能量，和能量墙
    :param i:
    :return:
    """
    global atomx, atoms, limit, limit_linex
    atomx += atoms
    atomx = np.remainder(atomx, limit)
    limit_atom = np.where((atomx == 0) & (atoms >= np.mean(atoms)))[0]
    if len(limit_atom) >= 1:
        atoms[limit_atom] -= 1
        # print('能量衰减')
        # limit += 1
        limit += len(limit_atom)
        limit_linex += len(limit_atom)
        print(atoms)
        print(limit)
    # print(atoms, limit, atomx)
    dot.set_data(atomx, atomy)
    """
        todo
    """
    # print(atomx)
    ln2.set_data(limit_linex, limit_liney)
    return dot, ln2


def gen_atom(energy):
    """
    粒子生成器
    :param energy: 各粒子能量列表
    :return: 各粒子初始坐标和初始能量
    """
    # x = np.array([random.randint(0, limit) for i in range(len(energy))])
    x = np.zeros(len(energy))
    s = np.array(energy)
    return x, s


if __name__ == '__main__':

    fig = plt.figure(figsize=(6, 6))
    ax = plt.gca()
    ax.grid()
    ln1, = ax.plot([], [], '-', lw=2)
    ln2, = ax.plot([], [], 'b-', lw=2)
    dot, = ax.plot([], [], 'ro')

    # energy = func_get_prime(20)
    energy = range(51, 151)
    limit = sum(energy) // len(energy)
    limit_linex = np.ones(2) * limit
    limit_liney = np.ones(2)
    limit_liney[1] = len(energy)

    atomx, atoms = gen_atom(energy)
    atomy = [i+1 for i in range(len(atomx))]

    ani = animation.FuncAnimation(fig, update_p, init_func=init, interval=1)

    plt.show()
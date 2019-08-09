import matplotlib.pyplot as plt



if __name__ == '__main__':
    times = 30
    x = [i - times // 2 for i in range(times)]
    y = list(map(lambda x:2*x, x))
    y1 = list(map(lambda x:(x-1)/3,x))
    y2 = list(map(lambda x:3*x+1,x))
    y3 = list(map(lambda x:3*x+3,x))
    y4 = list(map(lambda x:(x-3)/3,x))
    # print(y)
    plt.plot(x,y)
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(x,y3)
    plt.plot(x,y4)
    plt.show()
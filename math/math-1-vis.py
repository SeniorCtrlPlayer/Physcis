import matplotlib.pyplot as plt


class classfiy:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_ok(self, test, times=10):
        y = []
        i = 0
        while i < times:
            if test % self.b == 0:
                test = test // self.b
            else:
                test *= self.c
                test += self.a
            y.append(test)
            # time.sleep(1)
            i += 1
        # print("测试结束")
        return y


if __name__ == '__main__':
    c_test = classfiy(1,4,5)
    times = 30
    x = [i + 1 for i in range(times)]
    y = c_test.is_ok(1,times)
    print(y)
    plt.plot(x,y)
    plt.show()
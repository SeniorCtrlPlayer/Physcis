def print_test(test):
    print("{} ->".format(test))


class classfiy:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_ok(self, test, times=100):
        i = 0
        while i < times:
            if test % self.b == 0:
                test = test // self.b
            else:
                test *= self.c
                test += self.a
            print_test(test)
            # else:
            #     flag = False
            # time.sleep(1)
            i += 1
        print("测试结束")


def new_test():
    a, b, c = map(int, input("请输入三个数").split())

    c_test = classfiy(a, b, c)
    while True:
        test = int(input("请输入验证数字"))
        if test == 0:
            break
        else:
            c_test.is_ok(test)

if __name__ == '__main__':
    while True:
        new_test()
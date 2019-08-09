def print_test(test):
    print("{} ->".format(test), end="")


class classfiy:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_cyc(self, out_all, out_remove):
        """
        得到循环串
        :param out_all:完整的无序序列
        :param out_remove: 集合化的有序序列
        :return: 循环数字串
        """
        # 获取集合化序列长度
        a=len(out_remove)
        # 集合化长度后的一定是循环序列，循环次数未知
        b=out_all[a:]
        # 将循环序列部分进行集合化, c为循环序列中的数字集合，顺序未知
        c=set(b)
        # 已知循环序列长度，和第二次循环的开始索引
        d=out_all[a:a+len(c)+1]
        return d

    def is_ok(self, test, times=300):
        out_all = [test]
        out_remove = set()
        out_remove.add(test)
        i = 0
        while i < times:
            if test % self.b == 0:
                test = test // self.b
            else:
                test *= self.c
                test += self.a
            out_all.append(test)
            out_remove.add(test)
            # print_test(test)
            # else:
            #     flag = False
            # time.sleep(1)
            i += 1
        # print("测试结束")
        return self.get_cyc(out_all, out_remove)


def new_test(a, b, c):

    c_test = classfiy(a, b, c)
    while True:
        out = []
        test = int(input("请输入验证数字"))
        if test == 0:
            break
        else:
            out = c_test.is_ok(test)
        print(out)


def auto_test(array ,max_test, start=1):
    c_test = classfiy(array[0], array[1], array[2])
    out = []
    # while start<=max_test:
    #     if start == 0:
    #         break
    #     else:
    out = c_test.is_ok(start)
        # start += 1
    return out


if __name__ == '__main__':
    arrays = [[i*2+1, 2, 3] for i in range(40)]
    # a, b, c = map(int, input("请输入三个数").split())
    # for i in range(500):
    #     print(i+1, ": ", auto_test(a, b, c, i+1))
    for array in arrays:
        print(array[0], ":", auto_test(array, max_test=50, start=99))
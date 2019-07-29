import time

if __name__ == '__main__':
    a, b, c = map(int, input("请输入三个参数").split())
    flag = True
    while flag:
        d = int(input("请输入验证数"))
        while d>1:
            if d % a == 0:
                d = d // a
            else:
                d *= b
                d += c
            time.sleep(1)
            print(d, end=" > ")
        print()
        if d == 0:
            flag = False
    print("程序退出")
2 1 4 13
2 7 22 11
import random
import time as t

exit_flag = False  # 设置flag用于break跳出两层循环，或者自定义异常也行，try:, except。
dic = {}
dic[0] = '剪刀'
dic[1] = '石头'
dic[2] = '布'
print('欢迎来到wilf和zfy的石头剪刀布对战！')
t.sleep(1)
print('准备好了吗？那就开始啦！')
a = input('想要看模拟请铵1，自己对战wilf请按2，自己对战zfy请按3')
if a.isdigit() and (int(a) in [0, 1, 2]):  # 如果输入的是数字，并且在0,1,2中
    a = int(a)
else:
    print('那就随机出了！')
    a = random.randint(1, 3)

if a == 2:
    t.sleep(1)
    print('你对战wilf！')
    n = 0
    m = 0
    while True:
        m = m+1
        print('这是第{0}局，你赢了：{1}局'.format(m,n))
        humanStr = input("请输入[0:剪刀 1:石头 2:布] ")
        if humanStr.isdigit() and (int(humanStr) in [0, 1, 2]):  # 如果输入的是数字，并且在0,1,2中
            human = int(humanStr)
        else:
            print('那就随机出了！')
            human = random.randint(0, 2)
        windows = random.randint(0, 2)
        print('')
        print("你出的是%s,wilf出的是%s" % (dic[human], dic[windows]))

        if (human == 0 and windows == 2) or (human == 1 and windows == 0) or (human == 2 and windows == 1):
            print("祝贺你，你赢了!")
            oncemore = input("你想再来一局吗? y(Y) or n(N) ")
            n = n + 1

        elif human == windows:
            print("平局")
            oncemore = input("你想再来一局吗? y(Y) or n(N) ")

        else:
            print("不好意思，你输了")
            oncemore = input("你想再来一局吗? y(Y) or n(N) ")

        while True:
            if oncemore == 'y' or oncemore == 'Y':
                break
            elif oncemore == 'n' or oncemore == 'N':
                exit_flag = True
                break  # 跳出内层循环，并且设置flag

            else:
                oncemore = input("你想再来一局吗? y(Y) or n(N) ")

        if exit_flag == True:
            break  # 跳出层循环，结束程序

        else:
            print('')
            print("请重新输入!")

        pass

if a == 3:
    t.sleep(1)
    print('你对战zfy！')
    n = 0
    m = 0
    while True:
        m = m+1
        print('这是第{0}局，你赢了：{1}局'.format(m,n))
        humanStr = input("请输入[0:剪刀 1:石头 2:布] ")
        if humanStr.isdigit() and (int(humanStr) in [0, 1, 2]):  # 如果输入的是数字，并且在0,1,2中
            human = int(humanStr)
        else:
            print('那就随机出了！')
            human = random.randint(0, 2)
        windows = random.randint(0, 2)
        print('')
        print("你出的是%s,zfy出的是%s" % (dic[human], dic[windows]))

        if (human == 0 and windows == 2) or (human == 1 and windows == 0) or (human == 2 and windows == 1):
            print("祝贺你，你赢了!")
            oncemore = input("你想再来一局吗? y(Y) or n(N) ")
            n = n + 1

        elif human == windows:
            print("平局")
            oncemore = input("你想再来一局吗? y(Y) or n(N) ")

        else:
            print("不好意思，你输了")
            oncemore = input("你想再来一局吗? y(Y) or n(N) ")

        while True:
            if oncemore == 'y' or oncemore == 'Y':
                break
            elif oncemore == 'n' or oncemore == 'N':
                exit_flag = True
                break  # 跳出内层循环，并且设置flag

            else:
                oncemore = input("你想再来一局吗? y(Y) or n(N) ")

        if exit_flag == True:
            break  # 跳出层循环，结束程序

        else:
            print('')
            print("请重新输入!")

        pass

if a == 1:
    t.sleep(1)
    print('模拟对战！')
    n = 0
    m = 0
    k = 0
    while True:
        m = m+1
        print('这是第{0}局，wilf赢了：{1}局,zfy赢了：{2}局'.format(m,n,k))
        windows1 = random.randint(0,2)
        windows2 = random.randint(0,2)
        print('')
        print("wilf出的是%s,zfy出的是%s" % (dic[windows1], dic[windows2]))

        if (windows1 == 0 and windows2 == 2) or (windows1 == 1 and windows2 == 0) or (windows1 == 2 and windows2 == 1):
            print("wilf赢了!")
            oncemore = input("想再来一局吗? y(Y) or n(N) ")
            n = n + 1

        elif windows1 == windows2:
            print("平局")
            oncemore = input("想再来一局吗? y(Y) or n(N) ")

        else:
            print("zfy赢了！")
            oncemore = input("想再来一局吗? y(Y) or n(N) ")
            k = k+1

        while True:
            if oncemore == 'y' or oncemore == 'Y':
                break
            elif oncemore == 'n' or oncemore == 'N':
                exit_flag = True
                break  # 跳出内层循环，并且设置flag

            else:
                oncemore = input("你想再来一局吗? y(Y) or n(N) ")

        if exit_flag == True:
            break  # 跳出层循环，结束程序

        else:
            print('')
            print("请重新输入!")

        pass

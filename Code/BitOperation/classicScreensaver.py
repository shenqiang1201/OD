# 经典屏保
# 输入获取
x, y, t = list(map(int, input().split()))


# 算法入口
def getResult():
    global x
    global y

    x += t
    y += t

    while y + 25 > 600 or y < 0 or x + 50 > 800 or x < 0:
        if y + 25 > 600:
            # y = 600 - (y + 25 - 600) - 25
            y = 1150 - y

        if x + 50 > 800:
            # x = 800 - (x + 50 - 800) -50
            x = 1500 - x

        if y < 0:
            y = -y

        if x < 0:
            x = -x

    return f"{x} {y}"


# 算法调用
print(getResult())
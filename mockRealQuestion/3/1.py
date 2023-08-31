# 经典屏保
x, y, t = map(int, input().split())


def getResult():
    '''
    输入；
    0 0 10
    输出：
    10 10
    输入：
    500 570 10
    输出：
    510 570
    '''
    # x和y的最大边距
    max_x = 800 - 50
    max_y = 600 - 25
    # x和y的模拟位置
    model_x = x + t
    model_y = y + t

    global real_x, real_y

    if model_y > max_y:
        if (model_y // max_y) % 2 == 0:
            real_y = model_y - (max_y * (model_y // max_y))
        if (model_y // max_y) % 2 == 1:
            real_y = max_y - (model_y - (max_y * (model_y // max_y)))

    if model_x > max_x:
        if (model_x // max_x) % 2 == 0:
            real_x = model_x - (max_x * (model_x // max_x))
        if (model_x // max_x) % 2 == 1:
            real_x = max_x - (model_x - (max_x * (model_x // max_x)))

    if model_y <= max_y:
        real_y = model_y

    if model_x <= max_x:
        real_x = model_x

    return str(real_x) + " " + str(real_y)


print(getResult())

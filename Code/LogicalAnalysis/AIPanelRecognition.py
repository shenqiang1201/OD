# Ai面板识别
class Light:
    def __init__(self, id, x, y, r):
        self.id = id  # 编号
        self.x = x  # 圆心横坐标
        self.y = y  # 圆心纵坐标
        self.r = r  # 圆半径


# 输入获取
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
lights = list(
    map(lambda ele: Light(ele[0], (ele[1] + ele[3]) // 2, (ele[2] + ele[4]) // 2, (ele[3] - ele[1]) // 2), arr))


# 算法入口
def getResult():
    # 按照圆心y坐标升序
    lights.sort(key=lambda l: l.y)

    # ans记录题解
    ans = []

    # sameRowLights记录同一行的灯
    sameRowLights = []
    base = lights[0]
    sameRowLights.append(base)

    for i in range(1, len(lights)):
        light = lights[i]

        # 如果lights[i]的纵坐标和base的纵坐标相差不超过半径，则视为同一行
        if light.y - base.y <= base.r:
            sameRowLights.append(light)
        else:
            # 否则，不是同一行
            # 针对同一行的灯，再按照横坐标升序
            sameRowLights.sort(key=lambda l: l.x)
            for l in sameRowLights:
                ans.append(l.id)
            sameRowLights.clear()

            # 开始新的一行记录
            base = light
            sameRowLights.append(base)

    # 注意不要漏了最后一行
    if len(sameRowLights) > 0:
        sameRowLights.sort(key=lambda l: l.x)
        for l in sameRowLights:
            ans.append(l.id)

    return " ".join(map(str, ans))


# 算法调用
print(getResult())
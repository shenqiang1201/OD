# 构成正方形的个数
# 输入获取
n = int(input())
coordinates = [input() for _ in range(n)]


# 算法入口
def getResult():
    squareCount = 0

    coordinatesSet = set(coordinates)

    for i in range(n):
        x1, y1 = map(int, coordinates[i].split())
        for j in range(i + 1, n):
            x2, y2 = map(int, coordinates[j].split())

            x3 = x1 - (y1 - y2)
            y3 = y1 + (x1 - x2)

            x4 = x2 - (y1 - y2)
            y4 = y2 + (x1 - x2)

            if f"{x3} {y3}" in coordinatesSet and f"{x4} {y4}" in coordinatesSet:
                squareCount += 1

            x5 = x1 + (y1 - y2)
            y5 = y1 - (x1 - x2)

            x6 = x2 + (y1 - y2)
            y6 = y2 - (x1 - x2)

            if f"{x5} {y5}" in coordinatesSet and f"{x6} {y6}" in coordinatesSet:
                squareCount += 1

    return squareCount // 4


# 算法调用
print(getResult())

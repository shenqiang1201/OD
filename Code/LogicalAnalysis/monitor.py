# 车库需要打开多少监控
# 输入获取
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]


# 算法入口
def getResult():
    count = 0

    offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 1:
                count += 1
                continue

            for offsetX, offsetY in offsets:
                newX = x + offsetX
                newY = y + offsetY

                if m > newX >= 0 and n > newY >= 0 and matrix[newX][newY] == 1:
                    count += 1
                    break

    return count


# 算法调用
print(getResult())

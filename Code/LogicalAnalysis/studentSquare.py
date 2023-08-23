# 学生方阵
# 输入获取
n, m = map(int, input().split(","))
matrix = [input().split(",") for _ in range(n)]


# 算法入口
def getResult():
    ans = 0

    offsets = ((0, 1), (1, 0), (1, 1), (1, -1))

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "M":
                for offset in offsets:
                    oldI = i - offset[0]
                    oldJ = j - offset[1]

                    if n > oldI >= 0 and m > oldJ >= 0 and matrix[oldI][oldJ] == "M":
                        continue

                    length = 1
                    newI = i + offset[0]
                    newJ = j + offset[1]

                    while n > newI >= 0 and m > newJ >= 0 and matrix[newI][newJ] == "M":
                        length += 1
                        newI += offset[0]
                        newJ += offset[1]

                    ans = max(ans, length)

    return ans


# 调用算法
print(getResult())
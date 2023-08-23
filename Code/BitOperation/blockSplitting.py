# 分积木
# 输入获取
n = int(input())
weights = list(map(int, input().split()))


# 算法入口
def getResult(n, weights):
    weights.sort()

    minV = weights[0]

    correctSum = minV
    faultSum = minV

    for i in range(1, n):
        correctSum += weights[i]
        faultSum ^= weights[i]

    if faultSum == 0:
        return str(correctSum - minV)
    else:
        return "NO"


# 算法调用
print(getResult(n, weights))
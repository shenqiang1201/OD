# 响应报文时间
import sys

# 输入获取
c = int(input())
messages = [list(map(int, input().split())) for _ in range(c)]


def getMaxResponseTime(m):
    if m >= 128:
        bStr = bin(m)[2:]

        while len(bStr) < 8:
            bStr = '0' + bStr

        exp = int(bStr[1:4], 2)
        mant = int(bStr[4:], 2)

        return (mant | 16) << (exp + 3)
    else:
        return m


# 算法入口
def getResult():
    ans = sys.maxsize

    for t, m in messages:
        respTime = t + getMaxResponseTime(m)
        ans = min(ans, respTime)

    return ans


# 算法调用
print(getResult())
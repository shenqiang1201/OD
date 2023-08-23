# 报文重排序
# 输入获取
import re

n = int(input())
arr = input().split()


# 算法入口
def getResult():
    ans = []

    reg = re.compile(r"([a-zA-Z]+)(\d+)")

    for s in arr:
        matcher = reg.search(s)

        if matcher is None:
            continue

        content = matcher.group(1)
        i = int(matcher.group(2)) - 1

        ans.append([i, content])

    ans.sort(key=lambda x: x[0])

    return " ".join(map(lambda x: x[1], ans))


# 算法调用
print(getResult())

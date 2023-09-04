# 最少面试官数
# 得到面试官人数m和面试场数n
m = int(input())
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
print(m, n, arr)


def result():
    arr.sort(key=lambda x: x[1])  # 只有结束了当前面试了才能面试下一个人
    bukets = [[] for i in range(n)]
    for s, e in arr:
        for buket in bukets:
            # 每个面试官最多面试m个
            if len(buket) < m and (len(buket) == 0 or buket[-1] < s):
                buket.append(e)
                break
    return len(list(filter(lambda b: len(b) > 0, bukets)))  # 这个思路牛啊


# 算法调用
print(result())

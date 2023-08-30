# 数组组成的最小数字
N = list(map(int, input().split(",")))


def getResult():
    '''
    输入：
    21,30,62,5,31
    输出：
    21305
    输入：
    5,21
    输出：
    215
    '''

    if len(N) >= 3:
        N.sort()
        min_N = str(N[0])
        mid_N = str(N[1])
        max_N = str(N[2])
        return min(int(max_N + mid_N + min_N),
                   int(max_N + min_N + mid_N),
                   int(mid_N + max_N + min_N),
                   int(mid_N + min_N + max_N),
                   int(min_N + mid_N + max_N),
                   int(min_N + max_N + mid_N))

    if 0 < len(N) < 3:
        max_N = str(max(N))
        min_N = str(min(N))
        if max_N == min_N:
            return min_N
        else:
            return min(int(max_N + min_N),
                       int(min_N + max_N))


print(getResult())

# 计算堆栈中的剩余数字

'''
输入：
5 10 20 50 85 1
输出：
1 170
输入：
6 7 8 13 9
输出：
9 13 8 7 6
输入：
1 2 5 7 9 1 2 2
输出：
4 1 9 14 1
'''

N = list(map(int, input().split()))


def getResult():
    global m
    stack = []
    m = []

    for index in range(len(N)):
        m.append(N[index])
        # if index > 0:
        #     if N[index] == N[index - 1]:
        #         m.pop()
        #         m.pop()
        #         m.append(N[index] * 2)
        while index > 0:
            print("1")

    stack = m
    stack.reverse()
    back = "".join(str(stack).strip("[]").split(","))
    return back


print(getResult())

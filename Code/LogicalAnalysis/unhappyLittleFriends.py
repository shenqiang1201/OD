# 不开心的小朋友
# 输入获取
n = int(input())
kids = input().split()


# 算法入口
def getResult():
    # 不开心的小朋友数量
    unHappy = 0

    # 已在摇摇车上的小朋友编号
    playing = set()
    # 正在排队的小朋友编号
    waiting = []

    for kid in kids:
        if kid in playing:
            # 如果kid是摇摇车上的小朋友编号, 则代表kid玩好了要离开
            playing.remove(kid)

            # 如果kid离开后，摇摇车有空位了，如果此时有人排队，则让排队的人上车玩
            if len(waiting) > 0:
                playing.add(waiting.pop(0))
            continue

        # 如果kid不是摇摇车上的小朋友，则检查kid是不是排队的小朋友
        if kid in waiting:
            # 如果是排队的小朋友，则说明kid没有玩到摇摇车，因此会不开心的离开
            unHappy += 1
            waiting.pop(waiting.index(kid))
            continue

        # 如果kid既不是摇摇车上的小朋友，也不是排队的小朋友，则是新来的小朋友
        if len(playing) < n:
            # 如果摇摇车还有空位，则直接玩
            playing.add(kid)
        else:
            # 如果摇摇车没有空位了，则需要排队
            waiting.append(kid)

    return unHappy


# 算法调用
print(getResult())
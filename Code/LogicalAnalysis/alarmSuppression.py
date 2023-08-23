# 告警抑制
# 输入获取
n = int(input())
relations = [input().split() for _ in range(n)]
alertList = input().split()


# 算法入口
def getResult():
    fa = {}

    # id1抑制id2
    for id1, id2 in relations:
        if fa.get(id2) is None:
            fa[id2] = set()
        # fa用于记录抑制id2的所有id1的集合
        fa[id2].add(id1)

    alertSet = set(alertList)

    ans = []

    for id2 in alertList:
        # 如果没有抑制id2的更高级的告警，或者有抑制id2的更高级的告警，但是此高级告警没有出现在alertList列表中
        if fa.get(id2) is None or alertSet.isdisjoint(fa[id2]):
            # 此时id2就可以正常告警
            ans.append(id2)

    return " ".join(ans)


# 算法调用
print(getResult())

# 比赛
# 输入获取
import functools

m, n = map(int, input().split(","))
scores = [list(map(int, input().split(","))) for _ in range(m)]


def cmp(a, b):
    if a["sum"] != b["sum"]:
        return b["sum"] - a["sum"]

    for i in range(m):
        if a["score"][i] == b["score"][i]:
            continue
        return b["score"][i] - a["score"][i]

    return 0


# 算法入口
def getResult():
    if m < 3 or m > 10 or n < 3 or n > 100:
        return "-1"

    players = []

    for j in range(n):
        player = []
        for i in range(m):
            if scores[i][j] > 10 or scores[i][j] < 1:
                return "-1"
            player.append(scores[i][j])

        player.sort(reverse=True)
        players.append({
            "idx": j,
            "sum": sum(player),
            "score": player
        })

    players.sort(key=functools.cmp_to_key(cmp))

    return ",".join(list(map(lambda x: str(x["idx"] + 1), players[:3])))


# 算法调用
print(getResult())
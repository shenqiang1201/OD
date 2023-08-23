# 字符串化繁为简
# 输入获取
s = input()


def canCombine(set1, set2):
    for c in range(97, 123):
        lc = chr(c)  # 小写字符
        uc = chr(c - 32)  # 大写字符
        if (lc in set1 or uc in set1) and (lc in set2 or uc in set2):
            return True
    return False


def loop(eqs):
    for i in range(len(eqs)):
        for j in range(i + 1, len(eqs)):
            if canCombine(eqs[i], eqs[j]):
                tmp = list(eqs[i])
                tmp.extend(eqs[j])
                eqs[i] = set(tmp)
                eqs.pop(j)
                return True
    return False


# 算法入口
def getResult():
    # 主体字符容器
    cArr = []
    # 等效字符容器的集合
    eqs = []

    # isOpen标志，表示有没有遇到 '(' 字符
    isOpen = False

    # 下面逻辑用于从输入字符串中解析处主体字符，和等效字符
    for i in range(len(s)):
        c = s[i]

        if c == '(':
            isOpen = True
            eqs.append(set())
        elif c == ')':
            isOpen = False
            if len(eqs[-1]) == 0:  # 如果等效字符容器为空，则删除
                eqs.pop()
        else:
            if not isOpen:
                cArr.append(c)
            else:
                eqs[-1].add(c)

    # 暴力的对等效字符容器进行合并
    while loop(eqs):
        pass

    # 替换主体字符容器中的字符
    for eq in eqs:
        tmp = list(eq)
        tmp.sort()
        t = tmp[0]
        for i in range(len(cArr)):
            if cArr[i] in eq:
                cArr[i] = t

    ans = "".join(cArr)

    # 如果简化后的字符串为空，请输出为"0"。
    return "0" if len(ans) == 0 else ans


# 算法调用
print(getResult())
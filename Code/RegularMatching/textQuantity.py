# 统计文本数量
# 算法入口
import re


def fn(s):
    s = re.sub("\\[\"']", "", s)  # 替换\"和\'为空串
    s = re.sub("\".+?\"", "", s)  # 将成对双引号及其中内容替换为空串
    s = re.sub("'.+?'", "", s)  # 将成对单引号及其中内容替换为空串
    s = re.sub("-.+", "", s)  # 将-往后的注释替换为空串
    s = re.sub("\\s+", "", s)  # 将空白字符替换为空串
    s = re.sub(";+", ";", s)  # 将连续分号替换为单个分号
    return s


def getResult(lines):
    s = "".join(map(fn, lines))

    # 题目描述说：文本以”;”分隔，最后一条可以没有”;”
    # 为了避免复杂处理，这里无论最后一条文本有没有分号，都加一个
    s += ";"

    # 下面处理主要是为了处理跨行文本
    """
    比如
    aaaa;
    ;aaaa

    比如
    ;aaaa
    ;aaaa
    """
    s = re.sub(";+", ";", s)
    s = re.sub("^;", "", s)

    # 记录文本条数
    count = 0

    for c in s:
        if c == ';':
            count += 1  # 此时一行有几个分号，就代表几条文本

    return count


# 输入获取
lines = []

while True:
    line = input()

    if line != "":
        lines.append(line)
    else:
        print(getResult(lines))
        break

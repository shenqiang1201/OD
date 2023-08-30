# 关联字串
str1, str2 = input().split()


def getResult():
    '''
    输入：
    abc efghicbaiii
    输出：
    5
    输入：
    abc efghiccaiii
    输出：
    -1
    '''
    list(str1).sort()
    new_str1_len = len(list(str1))
    for i in range(len(list(str2))):
        new_str2 = list(str2)[i:(i + new_str1_len)]
        new_str2.sort()
        if new_str2 == list(str1):
            return i
    return -1


print(getResult())

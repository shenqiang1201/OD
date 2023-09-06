# 非严格递增连续数字序列

str1 = input()


def getResult():
    list1 = []
    count = 1
    count_list = []
    for i in range(len(str1)):
        if '0' <= str1[i] <= '9':
            list1.append(str1[i])

    for l in range(len(list1) - 1):
        if int(list1[l + 1]) - int(list1[l]) == 1 or list1[l] == list1[l + 1]:
            count += 1
        else:
            count = 0

        if count > 0:
            count_list.append(count)

    return max(count_list)


print(getResult())

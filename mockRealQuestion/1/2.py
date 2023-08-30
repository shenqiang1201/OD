# 高矮个子排队
num = list(input().split())
new_num = []


def getResult():
    '''
    输入：
    4 1 3 5 2
    输出：
    4 1 5 2 3
    输入：
    1 1 1 1 1
    输出：
    1 1 1 1 1
    输入：
    xxx
    输出
    【】
    '''
    left = 0
    right = left + 1

    # 当左下标小于右下标
    while left < right:
        try:
            # 首次左边小于右边，则右边移动到左边
            if (left % 2) == 0 and (right % 2) == 1 and num[left] < num[right]:
                new_num.append(num[right])
                num.insert(right + 1, num[left])
                num.pop(left)
            elif (left % 2) == 1 and (right % 2) == 0 and num[left] > num[right]:
                new_num.append(num[right])
            else:
                new_num.append(num[left])

            left = right
            right = left + 1

            if right == len(num):
                new_num.append(num[left - 1])
                return " ".join(new_num)
        except:
            return "[]"


print(getResult())

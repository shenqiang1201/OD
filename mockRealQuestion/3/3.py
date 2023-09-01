# 跳房子 2
target = input()
count = int(input())


def getResult():
    '''
    输入：
    [1,4,5,2,0,2]
    9
    输出：
    [4,5,0]
    输入：
    [1,5,2,0,2,4]
    9
    输出：
    [5，2，2]
    输入：
    [-1,2,4,9]
    12
    输出：
    [-1,4,9]
    '''
    steps = list(map(int, target.strip("[]").split(",")))

    left = 0
    right = len(steps) - 1
    max_index_sum = 3 * len(steps) - (1 + 2 + 3)  # 最大下标索引和
    tag = True
    dict_steps = {}

    while left < right:
        # 中间数据开始和结束下标区间
        mid_start = left + 1
        mid_end = right - 1

        for mid in range(mid_start, mid_end + 1):
            if steps[left] + steps[right] + steps[mid] == count:
                index_sum = left + right + mid
                k = min(index_sum, max_index_sum)
                if dict_steps.get(k) is None:
                    dict_steps[k] = []
                dict_steps[k].append([steps[left], steps[mid], steps[right]])
        # 左右边距移动
        if tag:
            left += 1
        else:
            right -= 1

        tag = not tag

    return dict_steps.get(min(dict_steps.keys()))[0]


print(getResult())

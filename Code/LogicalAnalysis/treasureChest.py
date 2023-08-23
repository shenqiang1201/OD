# 阿里巴巴找黄金宝箱3
# 左边的宝箱为最优先
# 输入获取
boxes = list(map(int, input().split(",")))
length = int(input())


# 算法入口
def getResult():
    # 统计该数字上一个箱子的编号
    lastIdx = {}
    # 对应数字的箱子已经找到了，符合咒语要求的箱子对
    find = set()

    ans = -1

    for i in range(len(boxes)):
        # 箱子上贴的数字
        num = boxes[i]

        # 该数字是否已经找到符合咒语要求的箱子对，如果找到了，则不需要再看后面的，只找第一对即可
        if num in find:
            continue

        # 检查箱子对是否符合咒语要求
        if lastIdx.get(num) is not None and i - lastIdx[num] <= length:
            find.add(num)
            ans = lastIdx[num] if ans == -1 else min(ans, lastIdx[num])
        else:
            lastIdx[num] = i

    return ans


# 算法调用
print(getResult())

# # 右边的宝箱为最优先
# # 输入获取
# boxes = list(map(int, input().split(",")))
# length = int(input())
#
#
# # 算法入口
# def getResult():
#     # 统计该数字上一个箱子的编号
#     lastIdx = {}
#
#     for i in range(len(boxes)):
#         # 箱子上贴的数字
#         num = boxes[i]
#
#         # 检查箱子对是否符合咒语要求
#         if lastIdx.get(num) is not None and i - lastIdx[num] <= length:
#             return lastIdx[num]
#         else:
#             lastIdx[num] = i
#
#     return -1
#
#
# # 算法调用
# print(getResult())

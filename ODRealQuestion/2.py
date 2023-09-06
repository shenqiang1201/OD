# 找终点

nums = list(map(int, input().split()))


def getResult():
    l = 0
    r = len(nums) - 1
    mid = (l + r) // 2

    for i in range(mid):
        if nums[i:nums[i] + i + 1][-1] == nums[-1]:
            if len(nums[i:nums[i] + i + 1]) == nums[i] + i + 1 - i:
                return i
    return -1


print(getResult())

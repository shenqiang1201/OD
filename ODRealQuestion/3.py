# 荒岛求生

def getResult():
    try:
        nums = list(map(int, input().split()))
        count_max = len(nums)
        for i in range(len(nums) - 1 - 1):
            if nums[i] + nums[i + 1] == 0:
                count_max -= 2
                nums = nums[0:i] + nums[i + 2:]

        for i in range(len(nums) - 1 - 1):
            print(nums)
            if nums[i + 1] < 0 and abs(nums[i + 1]) < nums[i]:
                count_max -= 1

        return count_max
    except:
        return -1


print(getResult())

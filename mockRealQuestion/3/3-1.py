import sys

# 输入获取
steps = list(map(int, input()[1:-1].split(",")))
count = int(input())


class Step:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx


# 算法入口
def getResult():
    n = len(steps)

    newSteps = [Step(steps[i], i) for i in range(n)]

    newSteps.sort(key=lambda x: (x.val, x.idx))

    minStepIdxSum = sys.maxsize
    ans = ""

    for i in range(n):
        # 剪枝优化
        if newSteps[i].val > 0 and 0 < count < newSteps[i].val:
            break

        # 剪枝优化
        if i > 0 and newSteps[i].val == newSteps[i - 1].val:
            continue

        l = i + 1
        r = n - 1

        while l < r:
            # 剪枝优化，L,R指针指向值的目标和为count - i指针指向的值，而L指针指向的值 必然小于等于 R指针指向的值，
            # 因此L指针指向的值必然 <= 目标和/2，而R指针指向的值必然 >= 目标和/2
            threshold = (count - newSteps[i].val) / 2
            if newSteps[l].val > threshold or newSteps[r].val < threshold:
                break

            stepValSum = newSteps[i].val + newSteps[l].val + newSteps[r].val

            if stepValSum < count:
                l += 1
            elif stepValSum > count:
                r -= 1
            else:
                # 剪枝优化
                while l < r - 1 and newSteps[r].val == newSteps[r - 1].val:
                    r -= 1

                stepIdxSum = newSteps[i].idx + newSteps[l].idx + newSteps[r].idx
                if stepIdxSum < minStepIdxSum:
                    minStepIdxSum = stepIdxSum

                    arr = [newSteps[i], newSteps[l], newSteps[r]]
                    arr.sort(key=lambda x: x.idx)

                    ans = "[" + ",".join(map(lambda x: str(x.val), arr)) + "]"

                # 剪枝优化
                while l + 1 < r and newSteps[l].val == newSteps[l + 1].val:
                    l += 1

                l += 1
                r -= 1

    return ans


# 算法调用
print(getResult())
# 增强的strstr
# 输入获取
import re

src = input()
tar = input()


# 核心代码
def getResult():
    res = re.search(tar, src)

    if res is None:
        return -1
    else:
        return res.start()


# 算法调用
print(getResult())

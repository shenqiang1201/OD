# 查字典
# 输入获取
tmp = input().split()

prefix = tmp[0]
n = int(tmp[1])

find = False
for i in range(n):
    word = tmp[i + 2]

    if word.startswith(prefix):
        find = True
        print(word)

if not find:
    print(-1)
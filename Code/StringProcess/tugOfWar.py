# 拔河比赛
# 算法入口
def getResult(employees):
    employees.sort(key=lambda x: (-x[0], -x[1]))

    for i in range(10):
        print(" ".join(map(str, employees[i])))


# 输入获取
employees = []

while True:
    line = input()

    if line != "":
        employees.append(list(map(int, line.split())))
    else:
        getResult(employees)
        break

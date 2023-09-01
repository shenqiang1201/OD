# we are a team （74分依旧有问题）
n, m = map(int, input().split())
msgs = [input().split() for _ in range(m)]


def getResult():
    '''
    输入；
    5 7
    1 2 0
    4 5 0
    2 3 0
    1 2 1
    2 3 1
    4 5 1
    1 5 1
    输出：
    We are a team
    We are a team
    We are a team
    We are not a team

    输入：
    5 6
    1 2 0
    1 2 1
    1 5 0
    2 3 1
    2 5 1
    1 3 2
    输出：
    We are a team
    We are not a team
    We are a team
    da pian zi
    '''
    if n < 1 or m >= 100000:
        print("Null")
        return

    dict_common = {}

    for index in range(len(msgs)):
        if int(msgs[index][-1]) == 0:
            if dict_common.get(msgs[index][0]) is None:
                dict_common[msgs[index][0]] = []
            if dict_common.get(msgs[index][1]) is None:
                dict_common[msgs[index][1]] = []
            dict_common[msgs[index][0]].append(msgs[index][1])
            dict_common[msgs[index][1]].append(msgs[index][0])

    for index in range(len(msgs)):
        if int(msgs[index][-1]) == 1:
            try:
                if msgs[index][1] in dict_common.get(msgs[index][0]) or dict_common.get(msgs[index][0]) == dict_common.get(msgs[index][1]):
                    print("We are a team")
                else:
                    print("We are not a team")
            except:
                print("We are not a team")

        if int(msgs[index][0]) < 1 or int(msgs[index][1]) > n or int(msgs[index][-1]) not in (0, 1):
            print("da pian zi")


getResult()

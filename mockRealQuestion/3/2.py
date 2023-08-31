# we are a team
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

    list_common = []

    for index in range(len(msgs)):
        if int(msgs[index][-1]) == 0:
            if (msgs[index][0] in list_common) or (msgs[index][1] in list_common):

            else:
                list_common.append(msgs[index])

            print(list_common)

        if int(msgs[index][-1]) == 1:
            for index_common in list_common:
                if (msgs[index][0] in index_common) and (msgs[index][1] in index_common):
                    print("We are a team")
                else:
                    print("We are not a team")

        if int(msgs[index][0]) < 1 or int(msgs[index][1]) > n or int(msgs[index][-1]) not in (0, 1):
            print("da pian zi")


getResult()

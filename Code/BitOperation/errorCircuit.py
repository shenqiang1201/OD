# 出错电路
# 输入获取
n = int(input())
bin1 = input()
bin2 = input()


# 算法入口
def getResult(n, bin1, bin2):
    """
    :param n: 二进制长度
    :param bin1: 可能产生错误交换的二进制
    :param bin2: 不会发生错误的二进制
    :return: 产生错误结果的情况有几种
    """
    # 找出bin2值为0的位，并统计对应位上bin1的值为0的有x个
    x = 0
    # 找出bin2值为0的位，并统计对应位上bin1的值为1的有y个
    y = 0
    # 统计bin1总共有多少个1
    a = 0
    # 统计bin1总共有多少个0
    b = 0

    for i in range(n):
        if bin1[i] == '0':
            b += 1
            if bin2[i] == '0':
                x += 1
        else:
            a += 1
            if bin2[i] == '0':
                y += 1

    return x * a + y * b - x * y


# 算法调用
print(getResult(n, bin1, bin2))
# 选修课
# 输入获取
s1 = input()
s2 = input()


class Student:
    def __init__(self, sid, cid, score1, score2):
        self.sid = sid  # 学号
        self.cid = cid  # 班号
        self.score1 = score1  # 课程一 得分
        self.score2 = score2  # 课程二 得分

    # 总分
    def getSumScore(self):
        return self.score1 + self.score2


def divide(s, courseId, students):
    for sub in s.split(";"):
        sid, score = sub.split(",")
        score = int(score)
        cid = sid[:5]

        # 是否已记录过该学生，若没有则生成对应学生对象
        if students.get(sid) is None:
            students[sid] = Student(sid, cid, -1, -1)

        if courseId == 1:
            students[sid].score1 = score
        else:
            students[sid].score2 = score


# 算法入口
def getResult():
    # key是学号，value是学生对象
    students = {}

    # 解析学生信息
    divide(s1, 1, students)
    divide(s2, 2, students)

    # 过滤出有两个课程得分的学生
    suits = list(filter(lambda stu: stu.score1 != -1 and stu.score2 != -1, students.values()))

    # 如果不存在这样的学生，则返回NULL
    if len(suits) == 0:
        print("NULL")
        return

    # key是班号，value是该班级的学生集合
    ans = {}
    for stu in suits:
        cid = stu.cid
        if ans.get(cid) is None:
            ans[cid] = []
        ans[cid].append(stu)

    tmp = list(ans.keys())
    tmp.sort()  # 按照班号升序

    for cid in tmp:
        # 打印班号
        print(cid)

        # 同一班的学生按照总分降序，总分相同，则按照学号升序
        ans[cid].sort(key=lambda x: (-x.getSumScore(), x.sid))
        # 打印同一班的学生学号，以分号分隔
        print(";".join(map(lambda x: x.sid, ans[cid])))


# 算法调用
getResult()
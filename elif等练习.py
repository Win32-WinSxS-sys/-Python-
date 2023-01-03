import time


def switch():
    score = float(input('请输入您的分数。'))
    if 60 > score >= 0:
        time.sleep(0.5)
        print('D.')
    elif 60 <= score < 70:
        time.sleep(0.5)
        print('C.')
    elif 70 <= score < 85:
        time.sleep(0.5)
        print('B.')
    elif 85 <= score < 95:
        time.sleep(0.5)
        print('A.')
    elif 95 <= score < 100:
        time.sleep(0.5)
        print('A+.')
    elif score == 100:
        time.sleep(0.5)
        print('S.')
        print('You\'re amazing!')
    else:
        print('你乱输入啥子天文数字呢？')

    '''
    先把输入的内容转化为小数，
    然后将输入内容和登记区间判断。
    d级在0~59.9间；
    c级在60~69.9间；
    b级在70~84.9之间；
    a级在85~94.9之间；
    a+级在95~99.9之间；
    s级最高，为100分。
    此外，我还增加了不少模拟耗时的代码，
    即那些重复的"time.sleep(0.5)"。
    这些是time模块的语句。
    sleep后加浮点数，
    代表延迟多久。
    这些都是延迟0.5秒后输出你的等级。
    如果你输入的数非0~100之间的任何一个整数或浮点数，
    就会输出“你乱输入啥子天文数字啊！”
    当然，
    如果你输入的不是数字，
    就只能报错了 <QwQ>
    (#^.^#) <OvO>
    '''


switch()


def score_ed():
    score2 = float(input('请输入您的分数：'))
    level = ("D." if 0 <= score2 < 60 else  # 0~59.9
             "C." if 60 <= score2 < 70 else  # 60~69.9
             "B." if 70 <= score2 < 85 else  # 70~84.9
             "A." if 85 <= score2 < 95 else  # 85~94.9
             "A+." if 95 <= score2 < 100 else  # 95~99.9
             "S.You are amazing!" if score2 == 100 else  # 100
             "请输入0~100之间的分值！")  # 输入的不是0~100之间的整数/小数。
    print(level)

# score_ed()

# elif score >= 85 and score < 95:   <这样的代码比较繁琐
# elif 95 <= score < 100:    <这样的代码比较简便

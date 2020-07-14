try:
    score = int(input("请输入你的成绩: "))
    if score < 60:
        print("D")
    elif score < 70:
        print("C")
    elif score < 80:
        print("B")
    elif score <= 90:
        print("A")
    else:
        print("A+")
except ValueError:
    print('请输入一个整数!')

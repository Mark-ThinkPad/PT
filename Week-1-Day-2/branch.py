year = 2020
if (year%4==0 and year%100!=0) or year%400==0:
    print(f'{year}是一个闰年')
else:
    print(f'{year}是一个平年')

score=int(input("please input you score:"))
if score < 60:
    print("D")
elif score >= 60 and score < 70:
    print("C")
elif score >= 70 and score < 80:
    print("B")
elif score >= 80 and score <= 90:
    print("A")
else:
    print("A+")

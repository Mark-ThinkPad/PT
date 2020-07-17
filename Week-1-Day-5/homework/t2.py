# 题目二
profit = int(input('请输入当月利润: '))
bonus = 0
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
for i in range(6):
    if profit > arr[i]:
        bonus += (profit - arr[i]) * rat[i]
        profit = arr[i]

print(f'奖金总数为: {bonus} 元')

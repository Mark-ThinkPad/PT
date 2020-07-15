from random import randint

# 生成一副扑克牌
suit = ['♡', '♧', '♢', '♤']
num = ['A', '2', '3', '4', '5', '6',
       '7', '8', '9', '10', 'J', 'Q', 'K']
poker = []
for i in suit:
    for j in num:
        poker.append(i + j)
poker.append('大王')
poker.append('小王')
print(poker)

# 洗牌（两两交换）
# 洗牌次数
m = randint(10, 100)
for i in range(1, m):
    # 随机选出两张牌交换
    r1 = randint(0, 53)
    r2 = randint(0, 53)
    poker[r1], poker[r2] = poker[r2], poker[r1]
print('---------洗完牌了---------')
print(poker)

# 斗地主发牌
# 三个玩家
a = poker[0:51:3]
b = poker[1:51:3]
c = poker[2:51:3]
# 三张底牌
d = poker[51:]
# 随机选出地主牌
rr = randint(0, 50)
ll = poker[rr]
# 判断地主是谁
print('地主牌是' + ll + ', ', end=' ')
if ll in a:
    print('玩家a是地主')
    a += d
if ll in b:
    print('玩家b是地主')
    b += d
if ll in c:
    print('玩家c是地主')
    c += d
# 打印当前手牌
print('------打印所有玩家的手牌------')
print('玩家a:', a, len(a))
print('玩家b:', b, len(b))
print('玩家c:', c, len(c))

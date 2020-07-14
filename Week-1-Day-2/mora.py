from random import randint

print('''
##########################
########猜拳小游戏##########
##########################
''')

coin = int(input('请投入游戏币, 输入您投入的数量: '))
while True:
    if coin >= 2:
        try: 
            gamer = int(input('(石头1, 剪刀2, 布3), 请输入数字: '))
            if gamer not in (1, 2, 3):
                raise ValueError
        except ValueError:
            print('请输入数字1/2/3!')
            continue
        computer = randint(1, 3)
        if gamer == computer:
            print('平手')
        if ((gamer==1 and computer==2) 
            or (gamer==2 and computer==3) 
            or (gamer==3 and computer==1)):
            print('玩家赢')
            coin *= 2
        else:
            print('电脑赢')
            coin -= 2
        print(f'玩家剩余{coin}个硬币')
    elif coin == 0:
        print('你已经输光了所有游戏币, 自动结束游戏')
        break    
    elif coin == 1:
        print('游戏币只剩一个不能进行下一局, 自动结束游戏')
        break

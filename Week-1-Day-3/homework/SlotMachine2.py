# 老虎机2
from random import randint

# 押注的物品及其对应的倍率
bets = {1: '苹果(5倍)', 2: '橙子(10倍)', 3: '柠檬(15倍)', 4: '铃铛(20倍)',
        5: '西瓜(20倍)', 6: '星星(30倍)', 7: '77(40倍)', 8: 'BAR(100倍)'}
multi = (5, 10, 15, 20, 20, 30, 40, 100)
# 水果老虎机24格(类型和倍率, 0为特殊方块/运气方块)
grids = ({'type': 2, 'multi': 1}, {'type': 4, 'multi': 1}, {'type': 8, 'multi': 50},
         {'type': 8, 'multi': 1}, {'type': 1, 'multi': 1}, {'type': 1, 'multi': 2},
         {'type': 3, 'multi': 1}, {'type': 5, 'multi': 1}, {'type': 5, 'multi': 2},
         {'type': 0, 'multi': 200}, {'type': 1, 'multi': 1}, {'type': 2, 'multi': 2},
         {'type': 2, 'multi': 1}, {'type': 4, 'multi': 1}, {'type': 7, 'multi': 2},
         {'type': 7, 'multi': 1}, {'type': 1, 'multi': 1}, {'type': 3, 'multi': 2},
         {'type': 3, 'multi': 1}, {'type': 6, 'multi': 2}, {'type': 6, 'multi': 1},
         {'type': 0, 'multi': 100}, {'type': 1, 'multi': 1}, {'type': 4, 'multi': 2})
# 玩家投入的游戏币
coin = 0
# 玩家押注的物品种类
bet = 0

# 规则: 亮起的方块和下注的物品种类相同或是特殊方块时, 按倍率获奖, 否则扣除两个游戏币
print('----------简易水果老虎机-----------')
coin += int(input('请输入投币数量(至少10个): '))
print('-----------下注物品一览------------')
for i in range(1, 9):
    print(f'{i}:{bets[i]}', end=' ')
print('\n---------------------------------')
while True:
    if coin >= 2:
        bet = int(input('请输入本轮下注的物品种类编号: '))
        # 随机亮起一个方块
        g = randint(0, 23)
        gType = grids[g]['type']
        gMulti = grids[g]['multi']
        # 获奖判断
        if gType == 0:
            coin *= gMulti + 1
            print(f'恭喜你, 点亮了特殊方块, 倍率加成为:{gMulti}倍!!!')
            print(f'本轮获奖总倍率为{gMulti}, 当前共有游戏币{coin}个')
        elif gType == bet:
            coin *= (gMulti * multi[gType-1] + 1)
            print(f'点亮的方块是: {bets[gType]}, 倍率加成为:{gMulti}倍')
            print(f'本轮获奖总倍率为{gMulti * multi[gType-1]}, 当前共有游戏币{coin}个')
        else:
            coin -= 2
            print('很遗憾没有获奖, 下一轮继续努力吧')
            print(f'当前共有游戏币{coin}个')
        print('---------------本轮结束----------------')
    else:
        try:
            add_coin = int(input('游戏币不足, 请选择是否继续, 输入1补充游戏币, 输入0退出: '))
            if add_coin not in (1, 0):
                raise ValueError
            if add_coin == 1:
                coin += int(input('请输入投币数量(至少10个): '))
            elif add_coin == 0:
                print('-------------游戏结束---------------')
                break
        except ValueError:
            print('请输入数字1或0!')
            continue

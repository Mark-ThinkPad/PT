# 老虎机
from random import randint

fruits = {1: '樱桃', 2: '草莓', 3: '菠萝', 4: '芒果', 5: '葡萄',
          6: '西瓜', 7: '橙子', 8: '苹果', 9: '梨子', 10: '果篮'}
flag = True
print('########简单老虎机小游戏##########')
bet = int(input('请输入下注金额(至少5元): '))
while True:
    if bet >= 2:
        pull = int(input('是否拉杆, 输入1拉杆, 输入0退出: '))
        if pull not in (1, 0):
            print('请输入数字1或0!')
            continue
        if pull == 1:
            s1 = randint(1, 10)
            s2 = randint(1, 10)
            s3 = randint(1, 10)
            s4 = randint(1, 10)
            s5 = randint(1, 10)
            result = [s1, s2, s3, s4, s5]
            print(fruits[s1], fruits[s2], fruits[s3], fruits[s4], fruits[s5])
            for i in range(1, 11):
                count = result.count(i)
                if count == 3 or count == 4:
                    if i == 10:
                        bet *= 8
                        print('中了7倍!!')
                    else:
                        bet *= 2
                        print('中了1倍')
                    flag = False
                    break
                if count == 5:
                    if i == 10:
                        bet *= 21
                        print('中了大奖20倍!!!!!')
                    else:
                        bet *= 6
                        print('中了5倍!')
                    flag = False
                    break
            res = {s1, s2, s3, s4, s5}
            if len(res) == 5 and 10 not in res:
                bet *= 11
                print('中了10倍!!!')
            elif flag:
                bet -= 2
                print('很遗憾, 没有中奖')
            print(f'您当前还有余额{bet}元')
            bet += int(input('请输入加注金额(至少5元, 不加注输入0): '))
        elif pull == 0:
            print('-------------游戏结束---------------')
            break
    else:
        try:
            add_bet = int(input('余额不足, 请选择是否继续, 输入1加注, 输入0退出: '))
            if add_bet not in (1, 0):
                raise ValueError
            if add_bet == 1:
                bet += int(input('请输入下注金额(至少5元): '))
            elif add_bet == 0:
                print('-------------游戏结束---------------')
                break
        except ValueError:
            print('请输入数字1或0!')
            continue

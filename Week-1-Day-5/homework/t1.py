# 设计一个函数: 参数有4个, 能组成多少个互不相同且无重复数字的三位数？都是多少？
def func(a: int, b: int, c: int, d: int):
    count = 0
    nums = [a, b, c, d]
    temp1 = []
    temp2 = []
    temp3 = []
    # 利用集合去重的特性处理重复的输入参数
    s = set(nums)
    if len(s) < 3:
        print('输入的参数中有两个以上的重复数字, 无法进行后续计算')
        return
    else:
        # 去掉一个重复的输入参数
        if len(s) == 3:
            nums = list(s)
        # 最外层循环, 确定百位数字
        for i in range(len(nums)):
            # 操作临时变量, 防止改变 nums 的值, 影响下次循环
            temp1 = nums.copy()
            # 取出百位数字
            x = temp1.pop(i)
            for j in range(len(temp1)):
                temp2 = temp1.copy()
                # 取出十位数字
                y = temp2.pop(j)
                for k in range(len(temp2)):
                    # 获取个位数字
                    z = temp2[k]
                    print(f'{x}{y}{z}', end=' ')
                    count += 1
            print()
        print(f'一共有{count}个符合要求的三位数')
        

if __name__ == "__main__":
    func(1, 2, 3, 4)
    func(1, 2, 3, 3)

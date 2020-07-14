# 打印出所有的 "水仙花数"
for n in range(100, 1000):
    i = n // 100
    k = n // 10 % 10
    j = n % 10
    if n == (i ** 3 + k ** 3+ j ** 3):
        print(n)

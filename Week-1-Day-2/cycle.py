j = 2
while j <= 100:
    count = 0
    k = 1
    while k <= j:
        if j % k == 0:
            count += 1
        k += 1
    if count == 2:
        print(f'{j}是一个素数')
    j += 1

t = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, t+1):
    n = int(input())
    arr = [0] * 8

    for i in range(len(money)):
        if n // money[i] != 0:
            arr[i] = n // money[i]
            n %= money[i]
    print('#{}'.format(tc))
    print(*arr)
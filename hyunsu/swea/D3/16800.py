t = int(input())

for tc in range(1, t+1):
    n = int(input())
    a = 1

    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            a = i
            b = n // a

    if a == 1:
        b = n

    print('#{} {}'.format(tc, a + b - 2))
 p
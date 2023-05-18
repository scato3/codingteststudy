t = int(input())

for tc in range(1, t+1):
    n = int(input())
    tmp = 'No'

    for i in range(1, 10):
        if n % i == 0:
            if n // i < 10:
                tmp = 'Yes'
                break

    print('#{} {}'.format(tc, tmp))

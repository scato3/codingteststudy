t = int(input())

for tc in range(1, t+1):
    n = int(input())

    if n % 2 == 1:
        print('#{} {}'.format(tc, 'Odd'))
    else:
        print('#{} {}'.format(tc, 'Even'))

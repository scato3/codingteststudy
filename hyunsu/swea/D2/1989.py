t = int(input())

for tc in range(1, t+1):
    a = input()
    test = a[::-1]

    if a == test:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
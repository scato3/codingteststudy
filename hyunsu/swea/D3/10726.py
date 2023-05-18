t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    ans = 'ON'

    for i in range(n):
        if m % 2 == 0:
            ans = 'OFF'
            break
        else:
            m //= 2

    print('#{} {}'.format(tc, ans))

t = int(input())

for tc in range(1, t+1):
    l, u, x = map(int, input().split())

    if l > x:
        print('#{} {}'.format(tc, l - x))
    elif l < x and u > x:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, -1))
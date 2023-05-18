t = int(input())

for tc in range(1, t+1):
    a, b = map(int, input().split())
    if 0 < a < 10 and 0 < b < 10:
        print('#{} {}'.format(tc, a*b))
    else:
        print('#{} {}'.format(tc, -1))
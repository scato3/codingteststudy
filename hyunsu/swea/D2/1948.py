t = int(input())
days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

for tc in range(1, t+1):
    a, b, c, d = map(int, input().split())

    print('#{} {}'.format(tc, (days[c - 1] + d) - (days[a - 1] + b) + 1))
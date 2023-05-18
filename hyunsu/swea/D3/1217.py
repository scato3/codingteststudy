t = 10

for tc in range(1, t+1):
    N = int(input())
    n, m = map(int, input().split())

    def power(n, m):
        if m == 0:
            return 1
        else:
            return n * power(n, m-1)

    print('#{} {}'.format(tc, power(n, m)))
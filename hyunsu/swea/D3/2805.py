t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    mid, s, e = n // 2, n // 2, n // 2
    res = 0

    for i in range(n):
        for j in range(s, e+1):
            res += arr[i][j]

        if i < mid:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print('#{} {}'.format(tc, res))
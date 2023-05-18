t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:
        n, m = m, n
        a, b = b, a

    max_sum = 0

    for i in range(m-n+1):
        tmp = 0
        for j in range(n):
            tmp += a[j] * b[i+j]

        if tmp > max_sum:
            max_sum = tmp

    print('#{} {}'.format(tc, max_sum))

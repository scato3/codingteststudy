t = int(input())

for tc in range(1, t+1):
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = input().split()
        a = float(a)
        b = int(b)
        ans += a * b

    print('#{} {:.6f}'.format(tc, ans))
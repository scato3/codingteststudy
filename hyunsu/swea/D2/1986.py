t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [i for i in range(1, n+1)]
    ans = 0
    for i in arr:
        if i % 2 == 1:
            ans += i
        else:
            ans -= i
    print('#{} {}'.format(tc, ans))

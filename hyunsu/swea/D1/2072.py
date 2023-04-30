n = int(input())

for i in range(1, n+1):
    a = list(map(int, input().split()))
    ans = 0
    for k in a:
        if k % 2 == 1:
            ans += k
    print('#{} {}'.format(i, ans))
t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    ans = []

    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for k in range(m):
                for a in range(m):
                    cnt += arr[i+k][j+a]
                ans.append(cnt)
    print('#{} {}'.format(tc, max(ans)))

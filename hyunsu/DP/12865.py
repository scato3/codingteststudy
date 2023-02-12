n, k = map(int, input().split()) # n 물건의 개수, k 무게의 최댓값
dp = [[0] * (k+1) for _ in range(n+1)]
tmp = [[0, 0]]

for _ in range(n):
    tmp.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = tmp[i][0]
        v = tmp[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])
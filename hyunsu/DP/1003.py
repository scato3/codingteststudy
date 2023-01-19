# 백준 1003 파보나치 함수 SILVER lll
# https://www.acmicpc.net/problem/1003

dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1

n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in list:
    print(dp[i][0], end=' ')
    print(dp[i][1])


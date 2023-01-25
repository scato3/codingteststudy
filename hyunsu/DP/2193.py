# 백준 2193 이친수 SILVER lll
# https://www.acmicpc.net/problem/2193

n = int(input())
dp = [1, 1]

for i in range(2, 91):
    dp.append(dp[i-2] + dp[i-1])

print(dp[n-1])
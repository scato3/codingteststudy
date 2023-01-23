# 백준 2156 포도주 시식
# https://www.acmicpc.net/problem/2156

n = int(input())
dp = [0]
s = [0]

for _ in range(n):
    s.append(int(input()))

dp.append(s[1])

if n > 1:
    dp.append(s[1] + s[2])



for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i]))

print(dp[n])
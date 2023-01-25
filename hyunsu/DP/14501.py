n = int(input())
t = []
p = []
dp = [0] * (n+1)

for _ in range(n):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)


for i in range(n-1, -1, -1):
    if t[i] + i > n: # 완료 날짜가 n을 넘어가면
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i])

print(dp[0])
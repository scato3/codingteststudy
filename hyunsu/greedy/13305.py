# 백준 13305 주유소 SILVER lll
# https://www.acmicpc.net/problem/13305

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

m = b[0]

for i in range(n-1):
    if b[i] < m:
        m = b[i]
    ans += m * a[i]
print(ans)
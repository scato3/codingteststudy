# 백준 1065 한수 SILVER lV
# https://www.acmicpc.net/problem/1065

n = int(input())
ans = 0

for i in range(1, n+1):
    k = list(map(int, str(i)))
    if i < 100:
        ans += 1
    elif k[0] - k[1] == k[1] - k[2]:
        ans += 1

print(ans)


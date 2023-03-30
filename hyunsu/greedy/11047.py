# 백준 동전 0 SILVER lV
# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
money = []
cnt = 0

for i in range(n):
    money.append(int(input()))

money.sort(reverse=True)

for i in money:
    cnt += k // i
    k %= i

print(cnt)

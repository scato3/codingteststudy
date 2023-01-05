# 백준 동전 0 SILVER lV
# https://www.acmicpc.net/problem/11047

money = []
n, k = map(int, input().split())
cnt = 0

for i in range(n):
    money.append(int(input()))

money.sort(reverse=True)

for i in money:
    cnt += k // i
    k %= i

print(cnt)
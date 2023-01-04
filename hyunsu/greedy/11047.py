# 백준 동전 0 SILVER lV

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
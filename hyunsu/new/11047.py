n, k = map(int, input().split())
money = []

for _ in range(n):
    money.append(int(input()))

money.sort(reverse = True)
cnt = 0

for i in money:
    cnt += k // i
    k %= i

print(cnt)
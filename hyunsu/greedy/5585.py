# 백준 5585 BRONZE ll
money = [500, 100, 50, 10, 5, 1]
n = int(input())
cnt = 0
k = 1000 - n

for i in money:
    if k // i > 0:
        cnt += k // i
        k %= i

print(cnt)

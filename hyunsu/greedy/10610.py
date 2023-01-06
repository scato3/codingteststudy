# 백준 10610 30 SILVER lV
# https://www.acmicpc.net/problem/10610

n = list(input())
n.sort(reverse=True)
tmp = 0

for i in n:
    tmp += int(i)

if tmp % 3 != 0 or '0' not in n:
    print(-1)
else:
    print(''.join(n))
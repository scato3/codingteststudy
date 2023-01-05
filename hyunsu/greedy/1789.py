# 백준 1789 수들의 합 SILVER V
# https://www.acmicpc.net/problem/1789

n = int(input())
k = 1

while (k+1) * k // 2 <= n:
    k += 1

print(k - 1)
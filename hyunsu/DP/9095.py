# 백준 9095 1, 2, 3 더하기 SILVER lll
# https://www.acmicpc.net/problem/9095

tc = int(input())

def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return dp(n-3) + dp(n-2) + dp(n-1)

for _ in range(tc):
    n = int(input())
    
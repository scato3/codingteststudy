# 백준 10162 전자레인지 BRONZE lV
# https://www.acmicpc.net/problem/10162

n = int(input())

if n % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = n // 300
    B = (n % 300) // 60
    C = (n % 300) % 60 // 10
    print(A, B, C)
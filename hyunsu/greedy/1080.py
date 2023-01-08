# 백준 1080 행렬 SILVER l
# https://www.acmicpc.net/problem/1080

def reverse(a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            A[i][j] = 1 - A[i][j]

n, m = map(int, input().split())
A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]
cnt = 0

for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            reverse(i, j)
            cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)

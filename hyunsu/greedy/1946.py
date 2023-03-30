# 백준 1946 신입 사원 SILVER l
# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []

    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key = lambda x:x[0])

    cnt = 1
    hired = arr[0][1]

    for i in range(1, n):
        if arr[i][1] < hired:
            hired = arr[i][1]
            cnt += 1
    print(cnt)




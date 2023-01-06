# 백준 1946 신입 사원 SILVER l
# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    arr = []
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key = lambda x:(x[0])) # 1번으로만 일단 정렬
    cnt = 1
    hired = arr[0][1] # 1번 정렬 중 대장(무조건 고용)
    for i in range(1, n):
        if arr[i][1] < hired:
            hired = arr[i][1]
            cnt += 1
    print(cnt)





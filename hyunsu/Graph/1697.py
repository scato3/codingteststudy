# 백준 1697 숨바꼭질 SILVER l
# https://www.acmicpc.net/problem/1697

from collections import deque

MAX = 100001
tmp = [0] * MAX

n, k = map(int, input().split())

q = deque()
q.append(n)

def bfs():
    while q:
        x = q.popleft()
        if x == k:
            print(tmp[k])
            break
        else:
            for nx in (x-1, x+1, x*2):
                if 0 <= nx < MAX and tmp[nx] == 0:
                    tmp[nx] = tmp[x] + 1
                    q.append(nx)

bfs()


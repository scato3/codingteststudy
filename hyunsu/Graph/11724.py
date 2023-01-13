# 백준 11724 연결 요소의 개수 SILVER ll
# https://www.acmicpc.net/problem/11724

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
print(cnt)
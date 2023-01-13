# 백준 1260 DFS와 BFS SILVER ll
# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited1[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited1[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited1[i] = 1

def dfs(v):
    visited2[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited2[i] == 0 and graph[v][i] == 1:
            dfs(i)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)

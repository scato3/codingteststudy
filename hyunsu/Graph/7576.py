# 백준 7576 토마토 GOLD V
# https://www.acmicpc.net/problem/7576

from collections import deque

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

def bfs():
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph


tmp = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tmp = bfs()

max_num = 0
for i in tmp:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    else:
        max_num = max(max_num, max(i))

print(max_num - 1)

ss# 백준 2667 단지번호 붙이기 SILVER l
# https://www.acmicpc.net/problem/2667

from collections import deque
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

tmp = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            tmp.append(bfs(i, j))
tmp.sort()

print(len(tmp))
for i in tmp:
    print(i)
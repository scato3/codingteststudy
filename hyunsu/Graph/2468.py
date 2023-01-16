# 백준 2468 안전 영역 SILVER l
# https://www.acmicpc.net/problem/2468

from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tmp = 0

for i in range(n):
    for j in range(n):
        tmp = max(tmp, graph[i][j])

max_result = 0

def bfs(x, y, k):
    cnt = 1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > k and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += 1
    return cnt

ans = 0

for k in range(tmp+1):
    visited = [[0] * n for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and visited[i][j] == 0:
                result.append(bfs(i, j, k))
    ans = max(ans, len(result))

print(ans)

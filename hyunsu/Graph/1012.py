# 1012 백준 유기농 배추 SILVER ll
# https://www.acmicpc.net/problem/1012

from collections import deque

tc = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(tc):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = -1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)


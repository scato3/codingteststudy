# 백준 7562 나이트의 이동 SILVER l
# https://www.acmicpc.net/problem/7562

from collections import deque

tc = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs():
    q = deque()
    q.append((startX, startY))

    while q:
        x, y = q.popleft()
        if x == endX and y == endY:
            print(graph[x][y] - 1)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

for _ in range(tc):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    graph[startX][startY] = 1
    bfs()




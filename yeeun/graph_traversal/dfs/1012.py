# 유기농배추
# 1012
# 재귀 limit 설정

import sys

sys.setrecursionlimit(10000)


# DFS
def dfs(x, y):
    # 상,하, 좌,우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if graph[ny][nx] == 1:
                # 방문했다는 표시 -1
                graph[ny][nx] = -1
                dfs(nx, ny)


t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    result = 0


    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1


    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i, j)
                result += 1

    # 출력
    print(result)
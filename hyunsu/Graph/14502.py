# 백준 14502 연구소 GOLD lV
# https://www.acmicpc.net/problem/14502

from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
max_result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    test_graph = copy.deepcopy(graph) # 복사
    count = 0
    global max_result

    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and test_graph[nx][ny] == 0:
                test_graph[nx][ny] = 2
                q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 0:
                count += 1

    max_result = max(max_result, count) # 큰 값 비교

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1) # DFS 재귀
                graph[i][j] = 0

wall(0)
print(max_result)


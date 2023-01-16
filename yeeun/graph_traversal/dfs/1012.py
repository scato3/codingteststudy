# 유기농배추
# 1012
# 재귀 limit 설정

import sys
sys.setrecursionlimit(10000)

def in_range(x,y):
    return 0 <= x and x < M and 0 <= y and y < N

def can_go(x,y):
    if not in_range(x, y):
        return False
    if graph[x][y] != 1:
        return False
def dfs(x, y):
    # 상,하, 좌,우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if can_go(nx,ny):
            #방문표시 2
            graph[nx][ny] = 2
            dfs(nx,ny)


t = int(input())
M, N, k = map(int,input().split())
cnt = 0

# graph = [
#     [0 for _ in range(M)]
#     for _ in range(N)
# ]
graph = [[0] * M for _ in range(N)]
for _ in range(k):
    i,j = (map(int, input().split()))
    graph[j][i] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i,j)
            # print(cnt)
            cnt += 1

print(cnt)
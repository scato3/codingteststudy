#https://www.acmicpc.net/problem/10026
#적록색약
'''
크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다
구역은 같은 색으로 이루어져 있다.
같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다
(단, 적록색약을 가진 사람 기준인 경우, 빨간색과 초록색은 같은 색상이라 한다)
출력 :  적록색약이 아닌 사람이 봤을 때의 구역의 개수와 / 적록색약인 사람이 봤을 때의 구역의 수를 /공백을 두고 출력
'''

import sys

sys.setrecursionlimit(10000)

n = int(input())
rg_group = 0
nomal_group = 0

#정상인의 그리드
grid = [
    list(map(str,input()))
    for _ in range(n)
]
#적록색약인의 그리드
rg_grid = [item[:] for item in grid]

for i in range(n):
    for j in range(n):
        if rg_grid[i][j] == 'R':
            rg_grid[i][j] = 'G'

visited = [[0]*n for _ in range(n)]
rg_visited = [[0]*n for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]


def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n


#정상인
def nomal_dfs(x,y):
    visited[x][y] = 1

    for dx, dy in zip(dxs, dys):
        nx = dx + x
        ny = dy + y
        if in_range(nx, ny) and visited[nx][ny] == 0:
            if grid[x][y] == grid[nx][ny]:
                nomal_dfs(nx,ny)


#적록색약
def rg_dfs(x,y):
    rg_visited[x][y] = 1

    for dx, dy in zip(dxs, dys):
        nx = dx + x
        ny = dy + y
        if in_range(nx, ny) and rg_visited[nx][ny] == 0:
            if rg_grid[x][y] == rg_grid[nx][ny]:
                rg_dfs(nx,ny)
    # rg_visited[x][y] = 1
    # for dx, dy in zip(dxs, dys):
    #     nx = dx + x
    #     ny = dy + y
    #     if in_range(nx, ny) and rg_visited[nx][ny] == 0:
    #         if (grid[x][y] == 'R') or (grid[x][y] =='G'):
    #             if (grid[nx][ny] == 'R') or (grid[nx][ny] =='G'):
    #                 # print(grid[x][y])
    #                 rg_dfs(nx, ny)
    #         else:
    #             rg_dfs(nx, ny)


#정상인이 보는 그룹 수
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:

            nomal_dfs(i,j)
            nomal_group+=1


#색맹인이 보는 그룹 수
for i in range(n):
    for j in range(n):
        if rg_visited[i][j] == 0:
            rg_dfs(i,j)
            rg_group += 1

print(f"{nomal_group} {rg_group}")
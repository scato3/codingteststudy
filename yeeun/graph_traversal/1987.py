#https://www.acmicpc.net/problem/1987
#알파벳
"""
세로 R칸, 가로 C칸
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
"""
import sys

sys.setrecursionlimit(10000)

r, c = tuple(map(int, input().split()))
grid = [
    list(map(str, input()))
    for _ in range(r)
]

visited=[
    [0] * c
    for _ in range(r)
]

def in_range(x,y):
    return 0<=x and x<r and 0<=y and y<c

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] != 0:
        return False

    return True

def alphabet_pass(n_alphabet):
    for i in range(r):
        for j in range(c):
            if visited[i][j] == n_alphabet:
                return False
    return True
def dfs(x,y):
    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]
    visited[x][y] = grid[x][y]

    for dx, dy in zip(dxs, dys):
        nx = x+dx
        ny = y+dy
        if can_go(nx,ny):
            if alphabet_pass(grid[nx][ny]):
                dfs(nx,ny)

ans=0
dfs(0,0)
for i in range(r):
    for j in range(c):
        if visited[i][j] != 0:
            ans +=1
print(visited)
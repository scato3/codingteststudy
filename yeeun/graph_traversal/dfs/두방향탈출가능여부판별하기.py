'''
n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출하려고 합니다
아래와 오른쪽 2방향 중 인접한 칸으로만 이동할 수 있으며, 뱀이 있는 칸으로는 이동을 할 수 없습니다.
뱀에게 물리지 않고 탈출 가능한 경로가 있는지 여부를 판별하는 코드를 작성해보세요.
'''


import sys

sys.setrecursionlimit(10000)


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


def can_go(x, y):
    if not in_range(x, y):
        return False
    # 뱀이 있거나 방문한 곳이라면
    if visited[x][y] or graph[x][y] == 0:
        return False
    return True


# 시간초과 코드
'''
def dfs(x, y):
    global ans
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if nx == n - 1 and ny == m - 1:
            ans += 1
            break
        if can_go(nx, ny):
            dfs(nx, ny)
'''
def dfs(x, y):

    visited[x][y] = 1
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            dfs(nx, ny)


n, m = tuple(map(int, input().split()))

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]
dfs(0, 0)

print(visited[n-1][m-1])
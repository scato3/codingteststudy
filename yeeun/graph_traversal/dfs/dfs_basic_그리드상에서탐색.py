"""
그리드에서 1인 곳만 지나갈 수 있다. 왼쪽 상단에서 시작하여 아래. 오른쪽으로만 이동이 가능하다.
두 방향 모두 이동이 가능할 경우 아래쪽을 우선 탐색한다.
탐색 방문 순서를 출력하려고 한다.
"""
grid = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1]
   ]

ans = [
    [0 for _ in range(5)]
    for _ in range(5)
]

visited = [
    [0 for _ in range(5)]
    for _ in range(5)
]

order = 1

#격자 안에 있는 가
def in_range(x,y) :
    return 0 <= x and x < 5 and 0 <= y and y < 5
#1이 있고 방문한 적이 없는가
def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x,y):
    global order

    dxs, dys = [1,0], [0,1]
    order +=1
    visited[x][y] = 1

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x,new_y):
            dfs(new_x,new_y)

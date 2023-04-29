'''
빨간 구슬을 구멍을 통해 뺴냄(파란 구슬은 안돼 - 실패)
4방향

조건)
1 빨간 구슬만 구멍에 빠져야 함( 파란 구슬도 들어가면 실패)
2 빨, 파 구슬 동시에 같은 칸 X

고려사항
1. 빨,파가 같은 행에 있을 경우

최소 몇 번 만에 빨갱이 탈출하는 지 구하라
(단, 10번 이하 움직여도 빨갱이 안 나오면 -1 출력)
. : 빈칸(이동 가능)
# : 장애물
O : 구멍
'''
from collections import deque

N,M = map(int,input().split())
graph = [
    list(input())
    for _ in range(N)
]
print(graph)
# graph = []
rx, ry, bx, by = 0,0,0,0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'B':
            bx = i
            by = j
        elif graph[i][j] == 'R':
            rx = i
            ry = j


dxs = [-1, 1, 0, 0]
dys = [0, 0, -1 ,1]
def in_range(x,y):
    return x < (M-1) and 0< x and y < (N-1) and 0< y

def can_move(x,y):
    if in_range(x,y):
        if graph[x][y] == 'O' or graph[x][y] == '.': return True
def move(rx,ry,bx,by):
    queue = deque()
    visited = []
    visited.append((rx, ry, bx, by))
    queue.append((rx, ry, bx, by))
    cnt = 0
    while queue:
        rx, ry, bx, by = queue.popleft()

        #cnt가 10 넘는지 확인
        if cnt > 10:
            return -1
        #빨강이가 구멍일 경우 확인
        if graph[rx][ry] == 'O':
            return cnt
        for dx, dy in zip(dxs, dys): #4방향 탐색
            n_rx, n_ry = rx + dx, ry + dy
            n_bx, n_by = bx + dx, by + dy
            while True:
                if can_move(n_rx,n_ry) == False:
                    break
                else:
                # rx = n_rx
                # ry = n_ry
                    if graph[rx][ry] == 'O':
                        return cnt
            while True:
                if can_move(n_bx, n_by) == False:
                    if graph[n_bx][n_by] == 'O':
                        break
                    # bx = n_bx
                    # by = n_by
            if graph[n_bx][n_by] == 'O':
                continue

            #이동 중 위치가 같을 경우
            if n_bx == n_rx and n_by == n_bx:
                if abs(n_rx - rx) + abs(n_ry -ry) > abs(n_bx - bx) + abs(n_by -by):
                    n_rx -= dx
                    n_ry -= dy
                else:
                    n_bx -= dx
                    n_by -= dy
            if [n_rx, n_ry, n_bx, n_by] not in visited:
                queue.append((n_rx, n_ry, n_bx, n_by))
                visited.append([n_rx, n_ry, n_bx, n_by])
        cnt += 1

print(move(rx,ry,bx,by))







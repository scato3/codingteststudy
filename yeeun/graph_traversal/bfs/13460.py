# https://www.acmicpc.net/problem/13460
# 구슬탈출2

'''
- 빨간 구슬을 구멍을 통해 빼내는 게임
- 파란 구슬이 구멍에 빠지면 실패 , 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패
- 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다
- 왼, 오, 위, 아래 4방향 가능
-'.' 빈칸, '#' 벽, 'O' 구멍, 'R' 빨간구슬, 'B'파란구슬
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.
'''

from collections import deque
import sys

input = sys.stdin.readline
n,m =map(int,input().split())
graph=[]

for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R':  # 빨간구슬 위치
            rx, ry = i, j
        elif graph[i][j] == 'B':  # 파란구슬 위치
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited=[]
    visited.append((rx,ry,bx,by))
    count = 0

    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            if count > 10:
                print(-1)
                return
            if graph[rx][ry] == 'O':
                print(count)
                return

            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]

                    if graph[nrx][nry] == '#': #벽이라면 한칸 뒤로
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] == 'O':  # 벽이라면 한칸 뒤로
                        break
                nbx, nby = bx, by
                while True:  # '#' 이 나오거나 구멍이면 아웃 그 전까지
                    nbx += dx[i]
                    nby += dy[i]

                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == 'O':
                        break

                if graph[nbx][nby] == 'O':
                    continue

                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry-ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count+=1
    print(-1)

bfs(rx, ry, bx, by)

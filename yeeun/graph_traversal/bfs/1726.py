'''
로봇
https://www.acmicpc.net/problem/1726

이동방향
직진 : Go 1, 2, 3
회전 : Turn left, right
0은 갈 수 있음 , 1은 못 감

입력 :
- M N
- 그리드
- 현재 위치 / 바라보는 방향(동:1 서:2 남:3 북:4)

로봇이 원하는 위치 / 원하는 방향 -> 최소 몇 번의 명령 필요?

'''

M, N = list(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(M)
]

current_x, current_y, current_dir =map(int, input().split())
goal_x, goal_y, goal_dir =map(int, input().split())

def can_go(x,y):
    return 0<=x and x<=M and y<=N and 0<=y


def bfs(x,y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx = dx + x
        ny = dy + y
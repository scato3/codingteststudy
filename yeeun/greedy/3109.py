'''
https://www.acmicpc.net/problem/3109

빵집 가스관에 몰래 파이프를 설치해 훔쳐서 사용하기로 했다.
빵집 : R*C격자. 첫번째 열 - 근처 빵집 가스관 / 마지막 열 - 원웅 빵집

가스관- 빵집 연결하는 파이프 설치 하려고 함
조건
1)건물이 있는 곳은 파이프 연결 못함
2)모든 파이프라인은 첫째 열에서 시작해야 하고, 마지막 열에서 끝나야 한다.
3)오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 연결 가능
-> (1,0) (1,1) (1, -1)

'''
input = __import__('sys').stdin.readline
R, C = map(int, input().split())


graph = [
    list(map(str, input()))
    for _ in range(R)
]

visited = [[False]*C for _ in range(R)]

dys = [0, 1, -1]

def in_range(x, y):
    return 0 <= x and x < R and 0 <= y and y < C

def can_go(x,y):
    if not in_range(x, y):
        return False
    if visited[x][y] == True:
        return False
    if graph[x][y] == 'x':
        return False

def solve(cx,cy):
    if cy == C-1: return True
    for dy in dys:
        nx, ny = cx+1, cy + dy
        if can_go(nx, ny):
            cx += 1
            cy = dy+cy
            visited[cx][cy] = True
            if solve(cx,cy):
                return True
    return False
ans =0
for i in range(R):
    print(visited[i][0])
    if graph[i][0] == ".":
        if solve(i,0):
            print(visited[i][0])
            ans+=1



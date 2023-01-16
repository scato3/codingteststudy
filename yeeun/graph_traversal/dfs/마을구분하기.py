#code tree
#마을구분하기
'''
n * n크기의 이차원 영역
사람 혹은 벽이 놓여져있습니다.
상하좌우의 인접한 영역에 있는 사람들은 같은 마을에 있는 것으로 간주

출력 : 총 마을의 개수, 같은 마을에 있는 사람의 수를 오름차순으로 정렬하여 출력
'''

# import sys
# sys.setrecursionlimit(10**7)

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
people = 0
area = []


def in_range(x, y):
    return (0 <= x and x < n and 0 <= y and y < n)


def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or (graph[x][y] == 0):
        return False
    return True


def dfs(x, y):
    global people
    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]
    # visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            people += 1
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = True
            people = 1
            dfs(i, j)

            area.append(people)
area.sort()
print(len(area))
for elem in area:
    print(elem)

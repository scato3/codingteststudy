import sys
input = sys.stdin.readline
answer = 0
def dfs(x, y):
    if y == C-1:
        return True
    for dx in [-1,0,1]:
        nx = x + dx
        ny = y + 1
        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] != "x" and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
    return False


R, C = map(int,input().split())
visited = [[-1 for _ in range(C)] for _ in range(R)]
graph = [list(input().strip()) for _ in range(R)]
for i in range(R):
    if dfs(i, 0): answer += 1
print(answer)
'''
색종이2
https://www.acmicpc.net/problem/2567
'''

n = int(input())

# 합친 거대한 사각형의 둘레 + 중간에 비어있는 사각형 둘레 -> 힘듦
# 한 사각형 당, 앞뒤좌우 살펴보았을 때 칸이 값이 본인의 값과 다르면 +1 해줌


graph = [[0]*101 for _ in range(101)]
visited = [[0]*101 for _ in range(101)]
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            graph[i+x][j+y] = 1
# dxs,dys = [1, 0, 0, -1], [0 , 1, -1, 0]

ans = 0


def in_range(x,y):
    return x<101 and y<101 and x>=0 and y>=0
# for i in range(101):
#     for j in range(101):
#         visited[i][j] = 1
#         for dx,dy in zip(dxs,dys):
#             if in_range(i+dx,j+dy):
#                 if graph[i+dx][j+dy] != graph[i][j]:
#                     if visited[i+dx][j+dy] == 0:
#                         visited[i+dx][j+dy] = 1
#                         ans+=1
#
for i in range(101):
    for j in range(101):
        # visited[i][j] = 1
        if in_range(i+1,j):
            if graph[i+1][j] != graph[i][j]: ans+=1
for i in range(101):
    for j in range(101):
        # visited[i][j] = 1
        if in_range(i,j+1):
            if graph[i][j+1] != graph[i][j]:
                ans += 1
                # if visited[i][j+1] == 0:
                #     visited[i][j+1] = 1


print(ans)
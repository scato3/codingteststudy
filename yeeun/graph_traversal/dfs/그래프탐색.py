# code tree
# 그래프탐색
"""
N개의 정점과 M개의 간선으로 이루어진 양방향 그래프가 주어졌을 때, 
1번 정점에서 시작하여 주어진 간선을 따라 이동했을 때 도달 할 수 있는 서로 다른 정점의 수를 구하는 프로그램을 작성해보세요
여기서 1번 정점 자기 자신에 도달하는 경우는 가지수에서 제외합니다.
"""
n, m = map(int, (input().split()))

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]


ver_cnt = 0

for i in range(m):

    v1, v2 = tuple(map(int, input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(vertex):
    global ver_cnt
    for current in graph[vertex]:
        #간선이 존재하고 방문한 적이 없는 정점 탐색
        if not visited[current]:
            visited[current] = True
            ver_cnt += 1
            dfs(current)
visited[1] = True
dfs(1)

print(ver_cnt)
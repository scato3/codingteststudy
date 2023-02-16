#https://www.acmicpc.net/problem/2606
#바이러스

#
from collections import deque
#
VERTICES_NUM = int(input()) + 1
EDGES_NUM = int(input())

graph = [[] for _ in range(VERTICES_NUM)]
start_points = []
end_points = []

for i in range(EDGES_NUM):
    a, b = map(int, input().split())
    start_points.append(a)
    end_points.append(b)
visited = [0 for _ in range(VERTICES_NUM)]
q = deque()


for start, end in zip(start_points, end_points):
    graph[start].append(end)  # graph[1] = [2, 3, 4]
    graph[end].append(start)


def bfs():
    while q:
        current_v = q.popleft()  # queue가 비워지기 전까지 맨 첫번째 원소를 뽑아 탐색

        for next_v in graph[current_v]:
            if not visited[next_v]:
                visited[next_v] = 1
                q.append(next_v)


root_vertex = 1
q.append(root_vertex) #root vertex를 queue에 넣기
bfs()
cnt=0
for i in visited:
    if i ==1:
        cnt+=1
print(cnt-1)

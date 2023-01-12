# 인접 행렬
VERTICES_NUM = 7
EDGES_NUM = 6

graph = [
    [0 for _ in range(VERTICES_NUM + 1)]
    for _ in range(VERTICES_NUM + 1)
]

# 방문 노드 확인을 위해
visited = [False for _ in range(VERTICES_NUM)]

# vertex : 정점
# current_vertext : 정점과 연결된 노드 방문 시 현재 방문하는 노드

# dfs탐색


def dfs(vertex):
    for current_vertext in range(1, VERTICES_NUM + 1):
      # 방문한 적이 없는 노드만 가기
        if graph[vertex][current_vertext] and not visited[current_vertext]:
            visited[current_vertext] = True
            dfs(current_vertext)


# 인접행렬로 그래프 표현
start_points = [1, 1, 1, 2, 4, 6]
end_points = [2, 3, 4, 5, 6, 7]

for start, end in zip(start_points, end_points):  # zip: 두개의 리스트에 for문 적용
    graph[start][end] = 1
    graph[end][start] = 1

# 초기 설정 (루트 설정)
root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)
# ------------------------------------------------------------------


# 인접 리스트
VERTICES_NUM = 7
EDGES_NUM = 6

graph = [[] for _ in range(VERTICES_NUM + 1)]
visited = [False for _ in range(VERTICES_NUM + 1)]

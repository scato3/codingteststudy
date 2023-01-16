# 백준 11403 경로 찾기 SILVER l
# https://www.acmicpc.net/problem/11403
# 플로이드 와샬 알고리즘

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n): # 경유지
    for i in range(n): # 시작
        for j in range(n): # 끝
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in graph:
    print(*i)
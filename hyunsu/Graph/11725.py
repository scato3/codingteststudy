# 백준 11725 트리의 부모 찾기 SILVER ll
# https://www.acmicpc.net/problem/11725

from collections import deque

n = int(input())
graph = [[]  for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0] * (n+1)

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for i in graph[x]:
            if ans[i] == 0:
                ans[i] = x
                q.append(i)


bfs(1)
res = ans[2:]
for i in res:
    print(i)


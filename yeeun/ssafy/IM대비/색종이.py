'''
https://www.acmicpc.net/problem/2563
색종이

'''
import sys
input = sys.stdin.readline
n = int(input())


visited = [
    [0]*101 for _ in range(101)
]
ans = 0
for _ in range(n):
    row, col = map(int, input().split())
    for x in range(10):
        for y in range(10):
            if visited[row+x][col+y] == 0:
                visited[row+x][col+y] = 1
for i in visited:
    ans+= i.count(1)
print(ans)

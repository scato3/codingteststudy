'''
https://www.acmicpc.net/problem/10163
1 4 3 2
= (1,4) ~ ( 1+3 -1, 4+2 -1)
= (1,4) ~ (3, 5)
'''

n = int(input())
graph=[[0]*1001 for _ in range(1001)]

# for a in range(n):
#     x, y, w, h = map(int, input().split())
#     for i in range(x, x+w):
#         for j in range(y,y+h):
#             graph[i][j] = a+1


# for i in range(1,n+1):
#     ans = 0
#     for r in range(1001):
#         for c in range(1001):
#             if graph[r][c] == i:
#                 ans+=1
#     print(ans)


for a in range(1,n+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        graph[i][y:y+h] = [a]*h
for i in range(1, n+1):
    ans = 0
    for a in range(1001):
        ans += graph[a].count(i)
    print(ans)
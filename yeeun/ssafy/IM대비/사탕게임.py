'''
https://www.acmicpc.net/problem/3085
빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y

'''
import sys
input=sys.stdin.readline

n = int(input())
grid =[]
for _ in range(n):
    arr = list(map(str, input()))
    grid.append(arr)


#check : 연속되는 부분 길이 세는 함수

def check(grid):
    MaxC = 1
    for i in range(n):
        cnt = 1
        #행을 순회하면서 길이 세기
        for j in range(1,n): #j가 움직인다고 생각
            if grid[i][j] == grid[i][j-1]:
                cnt+=1
                MaxC = max(cnt,MaxC)
            else:
                cnt = 1
        cnt=1
        #열을 순회하면서 길이 세기
        for j in range(1,n):
            if grid[j][i] == grid[j-1][i]:
                cnt+=1
                MaxC = max(cnt,MaxC)
            else:
                cnt = 1
    return MaxC
                
ans = 1
for i in range(n):
    for j in range(n):
        # 행을 순회
        if i + 1 < n:
            # 인접한 것과 바꾸고
            grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
            ans = max(ans, check(grid))
            # 원상복귀
            grid[i][j], grid[i+1][j] = grid[i+1][j],grid[i][j]
        #열을 순회
        if j+1 < n:
            # 인접한 것과 바꾸고
            grid[i][j], grid[i][j+1] = grid[i][j+1],grid[i][j]
            # check를 돌려서 - 가장 긴 연속부분 업데이트
            ans = max(ans,check(grid))
            #원상복귀
            grid[i][j], grid[i][j + 1] = grid[i][j+1], grid[i][j]


print(ans)



'''
123
456
789

g[0][1] g[0][0]
g[0][2] g[0][1]

g[1][0] g[0][0]

for i in range(n):
    for j in range(1,n):
        print(i,j)
        print('행1',grid[i][j],'행2',grid[i][j-1])

    for j in range(1,n):
        print(i, j)
        print('열1',grid[j][i],'열2',grid[j-1][i])
'''


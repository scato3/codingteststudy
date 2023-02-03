#https://www.acmicpc.net/problem/1018
#체스판 다시 칠하기

'''
M×N 크기의 보드
지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
1. 검은색과 흰색이 번갈아서 칠해져 있어야 한다
2. 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
3. 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''

N, M = tuple(map(int,input().split()))
board = [
    list(input())
    for _ in range(M)
]

arr = []
board_W = False
board_B = False
if board[0][0] =='W' :
    board_W = True
else:
    board_B = True

cnts = []
for i in range(M+1 - 8):
    for j in range(N+1-8):
        for n in range(i, i + 8):
            for m in range(j, j + 8):

                cnt = 0
                arr.append(board[n][m])
        print(arr)
        arr=[]
        # if(board_W):
        #     if (i % 2 == 0):
        #         if arr[0] != 'W':
        #             cnt+=1
        #         elif arr[1] !='B':
        #             cnt+=1
        #         elif arr[2] != 'B':
        #             cnt+=1
        #         elif arr[3] !='W':
        #             cnt+=1
        #     else:
        #         if arr[0] != 'B':
        #             cnt += 1
        #         elif arr[1] != 'W':
        #             cnt += 1
        #         elif arr[2] != 'W':
        #             cnt += 1
        #         elif arr[3] != 'B':
        #             cnt += 1
        #
        # else:
        #     if (i % 2 == 0):
        #         if arr[0] != 'B':
        #             cnt+=1
        #         elif arr[1] !='W':
        #             cnt+=1
        #         elif arr[2] != 'W':
        #             cnt+=1
        #         elif arr[3] !='B':
        #             cnt+=1
        #     else:
        #         if arr[0] != 'W':
        #             cnt += 1
        #         elif arr[1] != 'B':
        #             cnt += 1
        #         elif arr[2] != 'B':
        #             cnt += 1
        #         elif arr[3] != 'W':
        #             cnt += 1
        # cnts.append(cnt)
        # arr = []

print(min(cnts))
# board=[
# [0, 0, 0, 0],
# [1, 1, 1, 1],
# [2, 2, 2, 2],
# [3, 3, 3, 3],
# [0, 0, 0, 0]
# ]
# arr=[]
# for i in range(4):
#     for j in range(3):
#         for n in range(i,i+2):
#             for m in range(j, j+2):
#                 arr.append(board[n][m])
#         print(arr)
#         arr=[]

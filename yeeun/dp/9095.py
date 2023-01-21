#https://www.acmicpc.net/problem/9095
#1, 2, 3 더하기

'''
점화식을 구해보자
F[0] = 0
F[1] = 1
F[2] = 1+1 / 2 = 2
F[3] = 1+1+1 / 1+2 / 2+1 / 3 = 4
F[4] = 1+1+1+1 / 1+1+2 / 1+2+1 / 2+1+1 / 2+2 / 1+3 / 3+1 = 7
F[5] = 1+1+1+1+1/ 1+1+1+2 / 1+1+2+1 / 1+2+1+1 / 2+1+1+1 / 1+1+3 / 1+3+1 / 3+1+1 / 2+2+1 / 1+2+2 / 2+1+2 /3+2 / 2+3 = 13
F[n] = F[n-1] + F[n-2] + F[n-3]
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
test = [
    int(input())
    for _ in range(n)
]

for t in test:
    F = [0] * 11
    F[0] = 0
    F[1] = 1
    F[2] = 2
    F[3] = 4
    if t > 3:
        for n in range(4,t+1):
            F[n] = F[n-1] + F[n-2] + F[n-3]
    print(F[t])

# 에러 코드
# for t in (test):
#     F = [0]*(t+1)
#     if t <= 3:
#         if t == 3:
#             F[3] = 4
#         for i in range(t+1):
#             F[i] = i
#     if t> 3 :
#         F[0] = 0
#         F[1] = 1
#         F[2] = 2
#         F[3] = 4
#         for n in range(4,t+1):
#             F[n] = F[n-1] + F[n-2] + F[n-3]
#
#     print(F[-1])

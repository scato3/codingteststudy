#https://www.acmicpc.net/problem/1463
#1로 만들기
#https://jae04099.tistory.com/199 참고
#어렵다...
'''
전략
dp[n] : n+1이 1이 되는 연산의 최소 횟수
'''
'''
# 런타임에러 indexError -> n=2일때 dp[3]에서 에러
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

dp=[0]*(n+1)
    
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    dp[i] = dp[i-1] +1  #1을 빼주는 방법
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])
'''



#정상 작동 코드

n = int(input())

dp=[0]*(n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] +1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])

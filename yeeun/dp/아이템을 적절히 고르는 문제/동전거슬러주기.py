#code tree
#동전 거슬러주기

'''

N개의 동전의 종류가 주어졌을 때, 금액 M을 거슬러주기 위해 필요한 "최소 동전의 수를" 구해주는 프로그램을 작성해보세요.
예를 들어 N=3,M=8, 동전의 종류는 1,4,5 일때
8=1+1+1+5 이렇게 거슬러주면 총 4개의 동전이 필요하지만
8=4+4 이렇게 거슬러 주면 총 2개의 동전으로 돈을 거슬러 줄 수 있습니다.
'''

import sys
INT_MAX = sys.maxsize

n,m = tuple(map(int,input().split()))
coins = list(map(int,input().split()))
coins.insert(0, 0)
dp = [0] * (m+1)
def init():
    for i in range(1,m+1):
        dp[i] = INT_MAX
init()

for i in range (1, m+1):
    for j in range (1, n+1):
        if(i >= coins[j]):
            if dp[i-coins[j]] == INT_MAX:
                continue
            dp[i] = min(dp[i], dp[i-coins[j]]+1)
ans = dp[m]
if ans == INT_MAX:
    ans = -1
print(ans)
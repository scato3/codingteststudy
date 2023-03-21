'''
음수 X
20 초과 X
https://dev-wd.github.io/algorithm/backjoon5557/
'''

N = int(input())
nums = list(map(int, input().split()))
dp = [[0]*21 for i in range(N-1)]
#dp[i][j] = i인덱스까지 계산했을 때 j가 나올 수 있는 경우의 수
# = dp[idx][현재 수]
dp[0][nums[0]] = 1 #첫 번째 숫자는 당연히 포함함
for i in range(1, N-1):
    for j in range(21):
        # 그 다음 숫자를 더하거나 뺀 값이 0<= 값 <=20 라면 그 전 결과 값을 더함

        #j - num[i]가 0이상일 때
        #j + num[i]가 20이하일 때

        # j = 9 i = 3 num[1] = 3
        # 9 - 3 >=0 : dp[1][6] += dp[0][9] = 6
        # 9 + 3 <=20 : dp[1][12] += dp[0][9] = 12

        #i = 2 j = 6 nums[2] = 3
        #6 - 3 >= 0 : dp[2][3] += dp[1][6]
        if j-nums[i]>=0: dp[i][j-nums[i]] += dp[i-1][j]
        if j+nums[i]<=20: dp[i][j+nums[i]] += dp[i-1][j]

print(dp[-1][nums[-1]])

#https://www.acmicpc.net/problem/2579
#계단 오르기
'''
계단 오르기 게임
1. 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임
2. 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다
3. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다
4. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
->  첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다
5. 마지막 도착 계단은 반드시 밟아야 한다.

이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.


'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

steps = [
    int(input())
    for _ in range(n)
]
# 전략
'''

steps[i]가 현재 위치 -> 
1) 한칸 오름 > steps[i-1] 을 밟고 올라옴. 그 전엔 steps[i-3]을 밟고 올라온 것.
2) 두칸 오름 > steps[i-2]을 밟고 올라옴.

DP[i]: i번째 계단에 왔을 때의 최댓값.
DP[i] : max(한칸씩 올라 왔을 때 최댓값 , 두칸 올라 왔을 때 최댓값)
        max(DP[i-3]+steps[i-1]+steps[i] , DP[i-2]+steps[i])
'''

if n < 2:
    print(sum(steps))
else:
    dp=[]
    dp.append(steps[0])
    dp.append(steps[1] + steps[0])
    dp.append(max(steps[0]+steps[2], steps[1]+steps[2]))
    # print(dp)
    for i in range(3,n):
        dp.append(max(dp[i-3]+steps[i]+steps[i-1], dp[i-2]+steps[i]))

    print(dp[-1])


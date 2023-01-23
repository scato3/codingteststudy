#https://www.acmicpc.net/problem/2293
'''
n가지 종류의 동전이 있다
이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
그 경우의 수를 구하시오.

진짜 어렵다.

그치만 이해 해보도록 하자.

참고: https://aia1235.tistory.com/33

점화식)

DP[5] (1,2원으로 5를 만드는 경우의 수)
= DP[5] (갱신 되기 전 값 : 1원으로만 5를 만드는 경우의 수) + DP[5-2] (1,2원으로 3을 만드는 경우의 수, 여기서 2원을 추가하면 5가 되니까 3을 만드는 경우의 수만 생각해도 됨)

DP[i] = DP[i] + DP[i - coin]

세팅 ) DP[0] 은 DP[k-k] 라고 생각. 합이 k가 되게 만들 때 k원 동전을 내는 경우의 수 = 1
세팅 ) coins는 오름차순이어야 함

루프 )
coins 부터 for문을 돌려야 함
예를 들어, k =4 일 때 121 112 는 같은 경우로 친다.
그렇기 때문에 2원이 나오면 그 뒤엔 2원보다 큰 단위의 돈만 나오게 해주면 중복을 막을 수 있다.
coins로 for문을 돌면 1원 다음에 2원 이렇게 가기 때문에 121는 나올 수 없다.

조건 ) i - coin > 0 여야 인덱스가 양수가 되니, i의 range가 (c, k+1) 이어야 함

'''

import sys
input = sys.stdin.readline

n , k = tuple(map(int,input().split()))

#dp[i] = i원일 때 동전 개수
dp = [0] *(k+1)
dp[0] = 1
coins =[
    int(input())
    for _ in range(n)
]
coins.sort()
#무진장...어렵댜........

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = dp[i] + dp[i-coin]
print(dp[-1])

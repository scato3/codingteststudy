'''
https://www.acmicpc.net/problem/2798
블랙잭
카드 합이 21을 넘지 않은 내에서, 카드의 합을 최대한 크게 만드는 게임.

N개의 카드 합 < M

'''

N, M = map(int,input().split())
numbers = list(map(int, input().split()))
ans = 0
# 3개의 카드 정하는 경우
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if numbers[i]+numbers[j]+numbers[k] <= M:
                ans = max(numbers[i]+numbers[j]+numbers[k], ans)
print(ans)
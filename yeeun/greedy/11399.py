# 11399
# ATM문제
"""
지금 이 ATM앞에 N명의 사람들이 줄을 서있다. 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.

줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

예시)
P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2 인 경우를 생각해보자.

1. [1, 2, 3, 4, 5] 순서로 줄을 설 경우
1번 사람은 3분만에 돈을 뽑을 수 있다. 
2번 사람은 1번 사람이 돈을 뽑을 때 까지 기다려야 하기 때문에, 3+1 = 4분이 걸리게 된다.
3번 사람은 총 3+1+4 = 8분
4번 사람은 3+1+4+3 = 11분,
5번 사람은 3+1+4+3+2 = 13분
-> 필요한 시간의 합은 3+4+8+11+13 = 39분

2.[2, 5, 1, 4, 3] 순서로 줄을 설 경우 -> p[1,2,3,3,4]
2번 사람은 1분
5번 사람은 1+2 = 3분
1번 사람은 1+2+3 = 6분
4번 사람은 1+2+3+3 = 9분
3번 사람은 1+2+3+3+4 = 13분
-> 필요한 시간의 합은 1+3+6+9+13 = 32분

입력 
5
3 1 4 3 2

출력
32

"""
import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
time = 0
ans = []

pq = []
for i in arr:
    heapq.heappush(pq, i)


while len(pq) > 0:
    t1 = heapq.heappop(pq)
    time += (t1)
    ans.append(time)
time = 0
for i in ans:
    time += i
print(time)

# ver2
n = int(input())
arr = list(map(int, input().split()))
time = 0
arr.sort()


for i in range(n):
    for j in range(i+1):
        time += arr[j]
print(time)

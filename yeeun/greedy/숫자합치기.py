# code tree
# 숫자 합치기 문제
"""
n개의 숫자를 합쳐 하나의 숫자로 만드는 데 필요한 최소 비용을 출력합니다.

입력 
4
1 2 3 2

출력
16
"""
# ver 1 -> 시간초과

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
value = 0

while (len(arr) > 1):
    x1 = arr.pop(0)
    x2 = arr.pop(0)
    value += (x1 + x2)
    arr.append(x1 + x2)
    arr.sort()
print(value)

# ------------------
# ver2

n = int(input())
arr = list(map(int, input().split()))

priorityQueue = []
ans = 0
# 우선순위 큐에 원소 전부 넣기 (오름차순 자동 정렬)
# 작은 숫자 2개를 골라 합쳐야 하기에 작은 숫자가 먼저 골라질 수 있게 함
for elem in arr:
    heapq.heappush(priorityQueue, elem)


# 원소가 2개 이상이면 계속 가장 작은 숫자 2개 고르고
# 합치기 반복

while len(priorityQueue) > 1:
    x1 = heapq.heappop(priorityQueue)
    x2 = heapq.heappop(priorityQueue)

    ans += (x1 + x2)
    heapq.heappush(priorityQueue, x1+x2)

print(ans)

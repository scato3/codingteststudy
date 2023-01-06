# 백준 1715 카드 정렬하기 GOLD lV
# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
heapq.heapify(arr) # 정렬
ans = 0

while len(arr) != 1:
    a = heapq.heappop(arr) # heappop 가장 작은 값을 빼고 정렬
    b = heapq.heappop(arr)
    heapq.heappush(arr, a+b)
    ans += (a+b)
    if len(arr) == 1:
        break
print(ans)

# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
#
# arr.sort()
# tmp = 0
# if n == 1:
#     print(arr[0])
# else:
#     for i in range(n-1):
#         tmp += arr[i] + arr[i+1]
#         arr[i+1] = tmp
#     print(tmp)
#
# 메모리 초과

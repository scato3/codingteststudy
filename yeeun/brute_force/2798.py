#https://www.acmicpc.net/problem/2798
#블랙잭

'''
규칙 :
1.N장의 카드 중 3장을 골라야 함
2.카드합이 M보다 작아야 함
'''
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
cards = list(map(int,input().split()))


ans = 0

#for문 사용
# 5개의 코인 중 3개 (i, j , k) 를 픽하는 모든 경우의 수
# for i in range(0, N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             if cards[i]+cards[j]+cards[k] > M: continue
#             else:
#                 ans = max(ans,cards[i]+cards[j]+cards[k])
#
# print(ans)

#itertools 사용
permutationArray = permutations(cards, 3)
for i in permutationArray:
   if(M >= sum(i)):
       ans= max(ans, sum(i))

print(ans)


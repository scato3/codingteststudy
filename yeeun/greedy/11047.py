# 11047
# 동전 0
"""
동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. 
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. 

"""
import sys
input = sys.stdin.readline

n, k = map(int, (input().split()))
cnt = 0

arr = [
    int(input())
    for i in range(n)
]
arr.sort(reverse=True)

for i in range(n):
    if k > 0:
        if k // arr[i] > 0:  # 1500 // 1000
            cnt += (k//arr[i])
            k %= arr[i]
    else:
        break

print(cnt)

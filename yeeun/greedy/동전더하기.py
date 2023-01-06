# code_tree
# 동전더하기
""""
입력:
동전 종류의 수 / 총 금액

5 3800 
1
5
100
500
1000

출력:

7
"""
# ver 1
n, k = map(int, input().split())
coins = []
cnt = 0

for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

for i in range(n):
    cnt += k // coins[i]
    k = k % coins[i]


print(cnt)

# ver 2
n, k = tuple(map(int, input().split()))
coins = [
    int(input())
    for _ in range(n)
]
cnt = 0

for coin in coins[::-1]:
    cnt += k // coin
    k %= coin
print(cnt)

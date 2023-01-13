# 백준 2437 거울 GOLD ll
# https://www.acmicpc.net/problem/2437

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

tmp = 1

for i in arr:
    if tmp < i:
        break
    tmp += i

print(tmp)
# 백준 ATM SILVER lV
# https://www.acmicpc.net/problem/11399

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

for i in range(n):
    for j in range(i+1):
        ans += arr[j]

print(ans)




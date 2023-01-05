# 백준 2217 로프 SILVER lV
# https://www.acmicpc.net/problem/2217

n = int(input())
arr = []
k = []

for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

for i in range(n):
    k.append(arr[i] * (i + 1))

print(max(k))
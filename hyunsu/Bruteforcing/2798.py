# 백준 2798 블랙잭 BRONZE ll
# https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())
lst = list(map(int, input().split()))
arr = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if lst[i] + lst[j] + lst[k] > m:
                continue
            else:
                arr.append(lst[i] + lst[j] + lst[k])

print(max(arr))
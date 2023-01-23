# 백준 11727 2xn 타일링 2 SILVER ll
# https://www.acmicpc.net/problem/11727

n = int(input())
arr = [0, 1, 3]

for i in range(3, 1001):
    arr.append((arr[i-2] * 2) + arr[i-1])

print(arr[n] % 10007)
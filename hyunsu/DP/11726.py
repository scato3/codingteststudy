# 백준 11726 2xn 타일링 SILVER lll
# https://www.acmicpc.net/problem/11726

n = int(input())
arr = [0, 1, 2]

for i in range(3, 1002):
    arr.append(arr[i-2] + arr[i-1])

print(arr[n] % 10007)
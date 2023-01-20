# 백준 9461 파도반 수열 SILVER lll
# https://www.acmicpc.net/problem/9461

tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = [1, 1, 1]

    for i in range(3, n):
        arr.append(arr[i-3] + arr[i-2])

    print(arr[n-1])
# 백준 2231 분해합 BRONZE ll
# https://www.acmicpc.net/problem/2231

n = int(input())

for i in range(1, n+1):
    num = sum((map(int, str(i))))
    n_sum = i + num

    if n_sum == n:
        print(i)
        break
    if i == n:
        print(0)
        break
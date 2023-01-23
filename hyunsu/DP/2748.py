# 백준 2748 피보나치 수 2 BRONZE l
# https://www.acmicpc.net/problem/2748

n = int(input())

fib = []
num = 0

for i in range(n+1):
    if i == 0:
        num = 0
    elif i == 1 or n == 2:
        num = 1
    else:
        num = fib[i-1] + fib[i-2]
    fib.append(num)

print(fib[-1])

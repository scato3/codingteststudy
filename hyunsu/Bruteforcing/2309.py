# 백준 2309 일곱 난쟁이 BRONZE l
# https://www.acmicpc.net/problem/2309

arr = []

for i in range(9):
    arr.append(int(input()))

arr.sort()
a = 0
b = 0

for i in range(9):
    for j in range(i+1, 9):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            a = arr[i]
            b = arr[j]

arr.remove(a)
arr.remove(b)

for i in arr:
    print(i)
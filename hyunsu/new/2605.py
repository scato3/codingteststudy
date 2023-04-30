n = int(input())
arr = list(map(int, input().split()))
tmp = []
for i in range(n):
    tmp.insert(arr[i], i+1)

print(*tmp[::-1])
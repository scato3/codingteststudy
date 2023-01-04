# 백준 1931 회의실 배정 SILVER l

n = int(input())
arr = []
cnt = 0
tmp = 0

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key = lambda x:(x[1], x[0]))

for start, end in arr:
    if start >= tmp:
        cnt += 1
        tmp = end

print(cnt)

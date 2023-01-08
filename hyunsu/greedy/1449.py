# 백준 1449 수리공 항승 SILVER lll
# https://www.acmicpc.net/problem/1449

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = arr[0]
end = arr[0] + m
cnt = 1

for i in range(n):
    if start <= arr[i] < end: #파이프로 다 막히는 것
        continue
    else:
        start = arr[i]
        end = arr[i] + m
        cnt += 1

print(cnt)
        
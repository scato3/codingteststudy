# 백준 1182 부분수열의 합 SILVER ll
# https://www.acmicpc.net/problem/1182

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def back(idx, tmp):
    global cnt
    if idx >= n:
        return
    tmp += arr[idx]

    if tmp == m:
        cnt += 1

    back(idx+1, tmp)
    back(idx+1, tmp-arr[idx])

back(0, 0)
print(cnt)
# 백준 설탕배달 SILVER lV
# https://www.acmicpc.net/problem/2839

n = int(input())
cnt = 0

while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    n -= 3
    cnt += 1
else:
    print(-1)
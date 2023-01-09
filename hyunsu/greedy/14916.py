# 백준 14916 거스름돈 SILVER V
# https://www.acmicpc.net/problem/14916

n = int(input())
cnt = 0

while True:
    if n % 5 == 0:
        cnt += n // 5
        break
    n -= 2
    cnt += 1

if n < 0:
    print(-1)
else:
    print(cnt)
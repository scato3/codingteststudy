# 백준 1436 영화감독 숌 SILVER V
# https://www.acmicpc.net/problem/1436

n = int(input())
tmp = 666
cnt = 0

while True:
    if '666' in str(tmp):
        cnt += 1
    if cnt == n:
        print(tmp)
        break
    tmp += 1

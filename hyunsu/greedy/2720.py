# 백준 2720 세탁소 사장 동혁 BRONZE lll
# https://www.acmicpc.net/problem/2720

money = [25, 10, 5, 1]

n = int(input())
for i in range(n):
    cnt = []
    k = int(input())
    for j in money:
        cnt.append(k // j)
        k -= (k // j) * j

    print(' '.join(map(str, cnt)))


# 백준 4796 캠핑 BRONZE l
# https://www.acmicpc.net/problem/4796

tmp = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    print('Case {}: {}'.format(tmp, (V // P) * L + min(L, V % P)))
    tmp += 1

# 백준 4673 셀프 넘버 SILVER V
# https://www.acmicpc.net/problem/4673

k = set(range(1, 10001))
tmp = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    tmp.add(i)


ans = k - tmp

for i in ans:
    print(i)
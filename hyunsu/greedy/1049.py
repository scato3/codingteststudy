# 백준 1049 기타줄 SILVER lV
# https://www.acmicpc.net/problem/1049

n, m = map(int, input().split())
min_a = 1000
min_b = 1000
for _ in range(m):
    a, b = map(int, input().split())
    min_a = min(min_a, a)
    min_b = min(min_b, b)

tmp = 0

while n > 0:
    if n >= 6:
        tmp += min(min_a, min_b * 6)
        n -= 6
    else:
        if min_b * n > min_a:
            tmp += min_a
            break
        else:
            tmp += min_b
            n -= 1
print(tmp)

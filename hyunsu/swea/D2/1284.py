t = int(input())

for tc in range(1, t+1):
    p, q, r, s, w = map(int, input().split())
    t1 = p * w

    if w > r:
        t2 = q + (w - r) * s
    else:
        t2 = q

    print('#{} {}'.format(tc, min(t1, t2)))
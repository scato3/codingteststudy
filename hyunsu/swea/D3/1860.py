t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    cnt = 0
    lst = list(map(int, input().split()))
    lst.sort()

    ans = 'Possible'

    for i in lst:
        cnt += 1
        if (i // m) * k < cnt:
            ans = 'Impossible'
            break

    print('#{} {}'.format(tc, ans))

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    avr = sum(arr) / n
    cnt = 0

    for i in arr:
        if i <= avr:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
from collections import deque

t = 10

for tc in range(1, t+1):
    n = int(input())
    arr = deque(list(map(int, input().split())))
    cnt = 0

    while arr[-1] > 0:
        cnt %= 5
        cnt += 1

        tmp = arr.popleft() - cnt

        if tmp > 0:
            arr.append(tmp)
        else:
            arr.append(0)
    print('#{}'.format(tc),end=' ')
    print(*arr)

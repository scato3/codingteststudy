t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    ans = 0
    for i in arr:
        if arr.count(i) % 2 == 1:
            ans = i

    print('#{} {}'.format(tc, ans))

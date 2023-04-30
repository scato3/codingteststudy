n = int(input())

for tc in range(1, n+1):
    n = int(input())
    arr = list(map(int, input().split()))
    last = arr[-1]
    ans = 0

    for i in range(n-1, -1, -1):
        if arr[i] > last:
            last = arr[i]
        ans += last - arr[i]

    print('#{} {}'.format(tc, ans))

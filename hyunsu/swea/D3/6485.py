t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [0] * 5001
    for i in range(n):
        a, b = map(int, input().split())

        for j in range(a, b+1):
            arr[j] += 1

    p = int(input())
    ans = []

    for j in range(p):
        k = int(input())
        ans.append(arr[k])

    print('#{}'.format(tc),end=' ')
    print(*ans)



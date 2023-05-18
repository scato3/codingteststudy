t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    arr[0][0] = 1

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print('#{}'.format(tc))

    for a in range(n):
        for b in range(n):
            if arr[a][b]:
                print(arr[a][b],end=' ')
        print()

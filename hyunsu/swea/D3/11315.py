t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    result = 'NO'

    for i in range(n):
        for j in range(n):
            if i <= n - 5 and arr[i][j] == arr[i+1][j] == arr[i+2][j] == arr[i+3][j] == arr[i+4][j] == 'o':
                result = 'YES'
            if j <= n - 5 and arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == arr[i][j+4] == 'o':
                result = 'YES'
            if i <= n-5 and j <= n-5 and arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4] == 'o':
                result = 'YES'
            if i >= 4 and j <= n - 5 and arr[i][j] == arr[i-1][j+1] == arr[i-2][j+2] == arr[i-3][j+3] == arr[i-4][j+4] == 'o':
                result = 'YES'

    print('#{} {}'.format(tc, result))


            





            
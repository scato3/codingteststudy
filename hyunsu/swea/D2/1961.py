t = int(input())

def turn(a, n):
    new_arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_arr[i][j] = a[n-1-j][i]
    return new_arr

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    turn_90 = turn(arr, n)
    turn_180 = turn(turn_90, n)
    turn_270 = turn(turn_180, n)
    print('#{}'.format(tc))

    for i in range(n):
        for j in range(n):
            print(turn_90[i][j],end='')
        print(end=' ')
        for j in range(n):
            print(turn_180[i][j],end='')
        print(end=' ')
        for j in range(n):
            print(turn_270[i][j],end='')
        print()

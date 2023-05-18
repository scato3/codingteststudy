t = int(input())

def check(arr):
    for i in range(9):
        row_num = [0] * 10
        col_num = [0] * 10

        for j in range(9):
            row = arr[i][j]
            col = arr[j][i]

            if row_num[row]:
                return 0
            else:
                row_num[row] = 1
            if col_num[col]:
                return 0
            else:
                col_num[col] = 1

            if i % 3 == 0 and j % 3 == 0:
                box = [0] * 10
                for k in range(i, i+3):
                    for a in range(j, j+3):
                        num = arr[k][a]
                        if box[num]:
                            return 0
                        else:
                            box[num] = 1
    return 1

for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    res = check(arr)

    print('#{} {}'.format(tc, res))

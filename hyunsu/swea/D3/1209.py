t = 10

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_value = 0

    for i in range(100):
        sum_value = 0
        for j in range(100):
            sum_value += arr[i][j]

            if sum_value > max_value:
                max_value = sum_value

        for i in range(100):
            sum_value = 0
            for j in range(100):
                sum_value += arr[j][i]

            if sum_value > max_value:
                max_value = sum_value

    for i in range(100):
        sum_value = 0
        for j in range(100):
            if i == j:
                sum_value += arr[i][j]

                if sum_value > max_value:
                    max_value = sum_value

    for i in range(100):
        sum_value = 0
        for j in range(100):
            if j == 100 - i:
                sum_value += arr[i][j]

                if sum_value > max_value:
                    max_value = sum_value

    print('#{} {}'.format(tc, max_value))

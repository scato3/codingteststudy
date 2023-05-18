t = 10

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    for _ in range(n):
        max_arr = max(arr)
        min_arr = min(arr)

        arr[arr.index(max_arr)] -= 1
        arr[arr.index(min_arr)] += 1

        if max(arr) - min(arr) < 2:
            break

    result = max(arr) - min(arr)

    print('#{} {}'.format(tc, result))






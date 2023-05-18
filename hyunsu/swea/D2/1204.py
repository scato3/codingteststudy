t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = 0
    max_tmp = 0

    for i in arr:
        if arr.count(i) > tmp:
            tmp = arr.count(i)
            max_tmp = i
        if arr.count(i) == max_tmp:
            if i > max_tmp:
                max_tmp = i
                tmp = arr.count(i)

    print('#{} {}'.format(tc, max_tmp))


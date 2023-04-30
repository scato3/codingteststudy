n = int(input())
tmp = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, n+1):
    a = input()
    year = a[0:4]
    month = int(a[4:6])
    day = int(a[6:])
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day <= 31:
            print('#{} {}/{}/{}'.format(i, a[0:4], a[4:6], a[6:]))
        else:
            print('#{} {}'.format(i, -1))

    elif month in [4, 6, 9, 11]:
        if day <= 30:
            print('#{} {}/{}/{}'.format(i, a[0:4], a[4:6], a[6:]))
        else:
            print('#{} {}'.format(i, -1))

    elif month == 2:
        if day <= 28:
            print('#{} {}/{}/{}'.format(i, a[0:4], a[4:6], a[6:]))
        else:
            print('#{} {}'.format(i, -1))
    else:
        print('#{} {}'.format(i, -1))


t = int(input())
days = {
    'MON': 1,
    'TUE': 2,
    'WED': 3,
    'THU': 4,
    'FRI': 5,
    'SAT': 6
}

for tc in range(1, t+1):
    day = input()

    if day == 'SUN':
        print('#{} {}'.format(tc, 7))
    else:
        print('#{} {}'.format(tc, 7 - days[day]))

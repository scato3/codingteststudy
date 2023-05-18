from itertools import combinations

t = int(input())

for tc in range(1, t+1):
    n = list(input())
    target = [i for i in range(len(n))]

    min_num, max_num = int(''.join(n)), int(''.join(n))

    for value in combinations(target, 2):
        i, j = value
        n[i], n[j] = n[j], n[i]

        if n[0] == '0':
            n[i], n[j] = n[j], n[i]
            continue

        if int(''.join(n)) < min_num:
            min_num = int(''.join(n))

        if int(''.join(n)) > max_num:
            max_num = int(''.join(n))

        n[i], n[j] = n[j], n[i]

    print('#{} {} {}'.format(tc, min_num, max_num))
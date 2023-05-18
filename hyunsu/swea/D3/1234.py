t = 10

for tc in range(1, t+1):
    n, pwd = input().split()
    n = int(n)
    pwd = list(pwd)
    tmp = []

    for i in pwd:
        if len(tmp) > 0 and tmp[-1] == i:
            tmp.pop()
        else:
            tmp.append(i)

    print('#{} {}'.format(tc, ''.join(map(str, tmp))))
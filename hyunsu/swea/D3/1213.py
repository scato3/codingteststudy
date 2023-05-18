t = 10

for tc in range(1, t+1):
    n = int(input())
    tmp = input()
    check = input()

    print('#{} {}'.format(tc, check.count(tmp)))
t = int(input())

for tc in range(1, t+1):
    a = input()
    tmp = '0'
    ans = 0

    for i in range(len(a)):
        if a[i] != tmp:
            tmp = a[i]
            ans += 1

    print('#{} {}'.format(tc, ans))
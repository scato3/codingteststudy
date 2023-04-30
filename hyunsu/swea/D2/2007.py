n = int(input())

for tc in range(1, n+1):
    a = input()
    ans = ''

    for i in range(1, len(a)+1):
        if a[:i] == a[i:2 * i]:
            ans = a[:i]
            break
    print('#{} {}'.format(tc, len(ans)))

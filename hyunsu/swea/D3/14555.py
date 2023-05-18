t = int(input())

for tc in range(1, t+1):
    k = input()
    ans = 0

    for i in range(len(k)):
        if k[i] == '(':
            if k[i+1] != ')':
                ans += 1
        elif k[i] == ')':
            ans += 1

    print('#{} {}'.format(tc, ans))
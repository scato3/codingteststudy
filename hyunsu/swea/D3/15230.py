t = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"

for tc in range(1, t+1):
    tmp = input()
    ans = 0

    for i in range(len(tmp)):
        if tmp[i] == alpha[i]:
            ans += 1
        else:
            break


    print('#{} {}'.format(tc, ans))

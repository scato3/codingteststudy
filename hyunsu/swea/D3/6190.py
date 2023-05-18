def checkNum(num):
    num_str = str(num)
    for k in range(len(num_str) - 1):
        if num_str[k] > num_str[k+1]:
            return False
    return True

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(n-1):
        for j in range(i+1, n):
            num = arr[i] * arr[j]

            if checkNum(num):
                ans = max(ans, num)

    if ans == 0:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, ans))




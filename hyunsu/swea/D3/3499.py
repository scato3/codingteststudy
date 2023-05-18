t = int(input())

for tc in range(1, t+1):
    n = int(input())
    card = input().split()
    first = []
    second = []
    ans = []

    if n % 2 == 1:
        tmp = n // 2 + 1
    else:
        tmp = n // 2

    for i in range(tmp):
        first.append(card[i])

    for i in range(tmp, n):
        second.append(card[i])

    for i in range(tmp):
        if n % 2 == 1:
            if i != tmp - 1:
                ans.append(first[i])
                ans.append(second[i])
            else:
                ans.append(first[i])
        else:
            ans.append(first[i])
            ans.append(second[i])


    print('#{}'.format(tc),end=' ')
    print(*ans)
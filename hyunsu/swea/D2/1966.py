t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    print('#{}'.format(tc),end=' ')

    for i in arr:
        print(i,end=' ')
    print()
t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    stu = [i for i in range(1, n+1)]
    arr = list(map(int, input().split()))

    for i in arr:
        stu.remove(i)

    print('#{}'.format(tc),end=' ')
    print(*stu)
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(abs(a[i]))
    print('#{} {} {}'.format(tc, min(arr), arr.count(min(arr))))

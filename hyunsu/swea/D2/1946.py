t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = ''
    for _ in range(n):
        a, b = input().split()
        b = int(b)
        arr += a * b
    print('#{}'.format(tc))

    for i in range(0, len(arr), 10):
        print(arr[i:i+10])



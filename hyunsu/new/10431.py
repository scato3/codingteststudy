n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    k = a[0]
    arr = a[1:]
    cnt = 0

    for i in range(1, 20):
        for j in range(i):
            if arr[i] < arr[j]:
                cnt += 1
    print(k, cnt)
n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    tmp = False
    low, high = 0, n-1

    while low <= high:
        mid = (low + high) // 2
        if arr1[mid] > i:
            high = mid - 1
        elif arr1[mid] < i:
            low = mid + 1
        else:
            tmp = True
            break
    print(1 if tmp else 0, end=' ')

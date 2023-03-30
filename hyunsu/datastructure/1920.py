n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for num in arr2:
    start, end = 0, n-1
    tmp = False

    while start <= end:
        mid = (start + end) // 2
        if num == arr1[mid]:
            tmp = True
            print(1)
            break
        elif num > arr1[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if tmp == False:
        print(0)



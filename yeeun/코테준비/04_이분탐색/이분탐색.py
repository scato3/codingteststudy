def binary_search(array, target, start, end):
    if start > end :
        return None
    point = (start + end) // 2
    if array[point] == target:
        return point
    elif array[point] < target:
        return binary_search(array, target, point+1,end)
    else:
        return binary_search(array, target, start, point-1)

n,m = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
print(binary_search(array, m, 0, n-1) +1) #index가 아니라 위치번호라 1 더함
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += min(arr1) * max(arr2)
    arr1.pop(arr1.index(min(arr1)))
    arr2.pop(arr2.index(max(arr2)))

print(ans)
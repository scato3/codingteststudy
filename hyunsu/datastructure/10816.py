n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

cnt = {}

for i in arr1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in arr2:
    if i in cnt:
        print(cnt[i],end=' ')
    else:
        print(0,end=' ')

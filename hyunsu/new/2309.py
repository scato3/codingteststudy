arr = []
for _ in range(9):
    arr.append(int(input()))
arr.sort()
tmp = sum(arr)
k = []

for i in range(9):
    for j in range(i+1, 9):
        if tmp - arr[i] - arr[j] == 100:
            k.append(arr[i])
            k.append(arr[j])
            break

arr.remove(k[0])
arr.remove(k[1])

for i in arr:
    print(i)

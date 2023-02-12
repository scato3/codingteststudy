n = int(input())
arr = []
for _ in range(n):
    k = int(input())
    if k == 0:
        arr.pop()
    else:
        arr.append(k)

print(sum(arr))
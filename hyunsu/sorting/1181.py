n = int(input())
arr = []

for i in range(n):
    arr.append(input())

tmp = set(list(arr))

tmp_list = list(tmp)
tmp_list.sort()
tmp_list.sort(key=len)

for i in tmp_list:
    print(i)
import sys
input=sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

print(round(sum(arr) / n))
print(arr[n // 2])
dic = dict()

for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

tmp = []
mx = max(dic.values())

for i in dic:
    if mx == dic[i]:
        tmp.append(i)

if len(tmp) > 1:
    print(tmp[1])
else:
    print(tmp[0])

print(max(arr) - min(arr))

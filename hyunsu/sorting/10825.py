n = int(input())
arr = []

for _ in range(n):
    a, b, c, d = map(str, input().split())
    arr.append([a, int(b), int(c), int(d)])

arr.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])
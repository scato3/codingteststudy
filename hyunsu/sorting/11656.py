s = str(input())
arr = []

for _ in s:
    arr.append(s)
    s = s[1:]

for i in sorted(arr):
    print(i)
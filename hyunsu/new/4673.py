arr = set(list(range(1, 10001)))
self_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    self_num.add(i)

ans = sorted(arr - self_num)
for i in ans:
    print(i)
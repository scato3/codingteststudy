n, m = map(int, input().split())
a = set()
for _ in range(n):
    a.add(input())

b = set()
for _ in range(m):
    b.add(input())

k = sorted(a & b)

print(len(k))

for i in k:
    print(i)
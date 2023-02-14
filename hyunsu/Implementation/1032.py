n = int(input())
a = list(input())
an = len(a)

for i in range(n-1):
    b = list(input())
    for j in range(an):
        if a[j] != b[j]:
            a[j] = '?'

print(''.join(a))
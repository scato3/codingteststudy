n = int(input())

for i in range(n):
    a = input().split()
    tmp = []

    for k in a:
        tmp.append(k[::-1])

    print(' '.join(tmp))

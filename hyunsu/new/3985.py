L = int(input())
n = int(input())

cake = [0] * (L+1)
received = [0] * (n+1)
want = []

for i in range(1, n+1):
    a, b = map(int, input().split())
    cnt = 0
    want.append(b-a)

    for j in range(a, b+1):
        if cake[j] == 0:
            cake[j] = i
            cnt += 1
    received[i] = cnt

print(want.index(max(want)) + 1)
print(received.index(max(received)))

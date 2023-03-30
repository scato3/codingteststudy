from collections import deque

n, k = map(int, input().split())
q = deque()
res = []

for i in range(1, n+1):
    q.append(i)

while q:
    for i in range(k-1):
        q.append(q.popleft())   
    res.append(q.popleft())

print('<', end='')
print(', '.join(map(str, res)),end='')
print('>')
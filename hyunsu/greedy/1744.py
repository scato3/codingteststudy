# 백준 1946 수 묶기 GOLD lV
# https://www.acmicpc.net/problem/1744

n = int(input())
pos = [] # 양수
neg = [] # 음수
ans = 0

for _ in range(n):
    k = int(input())
    if k > 1:
        pos.append(k)
    elif k == 1:
        ans += 1
    else:
        neg.append(k)

pos.sort(reverse=True)
neg.sort()

if len(pos) % 2 == 0:
    for i in range(0, len(pos), 2):
        ans += pos[i] * pos[i+1]
else:
    for i in range(0, len(pos) - 1, 2):
        ans += pos[i] * pos[i+1]
    ans += pos[len(pos) - 1]

if len(neg) % 2 == 0:
    for i in range(0, len(neg), 2):
        ans += neg[i] * neg[i+1]
else:
    for i in range(0, len(neg) - 1, 2):
        ans += neg[i] * neg[i+1]
    ans += neg[len(neg) - 1]

print(ans)
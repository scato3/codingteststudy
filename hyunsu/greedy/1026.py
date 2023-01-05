# 백준 1026 보물 SILVER lV

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

for _ in range(n):
    ans += max(a) * min(b)
    a.pop(a.index(max(a)))
    b.pop(b.index(min(b)))

print(ans)
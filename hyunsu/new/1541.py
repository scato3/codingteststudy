arr = input().split('-')
num = []

for i in arr:
    ans = 0
    tmp = i.split('+')
    for j in tmp:
        ans += int(j)
    num.append(ans)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)
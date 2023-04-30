n, m = map(int, input().split())
garo = [0, m]
sero = [0, n]

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a:
        sero.append(b)
    else:
        garo.append(b)

garo.sort()
sero.sort()
result = 0

for i in range(len(garo) - 1):
    for j in range(len(sero) - 1):
        result = max(result, (sero[j+1] - sero[j]) * (garo[i+1] - garo[i]))

print(result)

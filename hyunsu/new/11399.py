n = int(input())
arr = sorted(list(map(int, input().split())))
result = 0

for i in range(1, n+1):
    result += sum(arr[:i])

print(result)
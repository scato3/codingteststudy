# 백준 1541 잃어버린 괄호 SILVER ll

a = input().split('-')
arr = []

for i in a:
    num = 0
    s = i.split('+')
    for j in s:
        num += int(j)
    arr.append(num)

ans = arr[0]

for i in range(1, len(arr)):
    ans -= arr[i]

print(ans)

n = int(input())

for i in range(1, n+1):
    ans = 0
    i = str(i)
    ans += i.count('3') + i.count('6') + i.count('9')
    if ans == 0:
        print(i, end=' ')
    else:
        print(ans * '-',end=' ')

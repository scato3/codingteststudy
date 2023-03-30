n = int(input())
arr = []
tmp = []
cnt = 1
temp = True

for i in range(n):
    num = int(input())

    while cnt <= num:
        arr.append(cnt)
        tmp.append('+')
        cnt += 1
    if arr[-1] == num:
        arr.pop()
        tmp.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in tmp:
        print(i)
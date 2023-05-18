num = [2, 3, 5, 7, 11]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    i = 0
    arr = [0] * 5
    print('#{}'.format(tc),end=' ')
    for i in range(5):
        while n % num[i] == 0:
            arr[i] += 1
            n //= num[i]
        print(arr[i],end=' ')
    print()




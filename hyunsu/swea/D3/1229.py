t = 10

for tc in range(1, t+1):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = input().split()

    for i in range(len(arr2)):
        if arr2[i] == 'I':
            tmp1 = int(arr2[i+1])
            tmp2 = int(arr2[i+2])

            for j in range(tmp2):
                arr1.insert(tmp1 + j, arr2[i + 3 + j])

        if arr2[i] == 'D':
            tmp1 = int(arr2[i+1])
            tmp2 = int(arr2[i+2])

            for j in range(tmp2):
                del(arr1[tmp1])

    print('#{} {}'.format(tc,' '.join(map(str, arr1[:10]))))
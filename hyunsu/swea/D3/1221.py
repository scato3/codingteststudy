num = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5,
       'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

t = int(input())

for tc in range(1, t+1):
    tmp, L = input().split()
    L = int(L)

    words = input().split()
    words.sort(key = lambda x:num[x])

    print('#{}'.format(tc))

    for i in words:
        print(i,end=' ')
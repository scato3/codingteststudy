num = {'0001101':0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    for i in range(n):
        if sum(map(int, arr[i])) == 0:
            continue
        else:
            tmp = arr[i]
            for j in range(m-1, -1, -1):
                if tmp[j] == '1':
                    pwd = tmp[j-55:j+1]
                    break

    my_code_value = [num[pwd[i:i+7]] for i in range(0, 56, 7)]

    odd = 0
    even = 0

    for i in range(8):
        if i % 2 == 0:
            even += my_code_value[i]
        else:
            odd += my_code_value[i]

    result = even * 3 + odd

    if result % 10 == 0:
        print('#{} {}'.format(tc, sum(my_code_value)))
    else:
        print('#{} {}'.format(tc, 0))





t = int(input())

for tc in range(1, t+1):
    words = [input() for _ in range(5)]
    max_len = 0

    for i in words:
        max_len = max(max_len, len(i))

    print('#{}'.format(tc),end=' ')
    for i in range(max_len):
        for j in range(5):
            if i < len(words[j]):
                print(words[j][i],end='')
    print()

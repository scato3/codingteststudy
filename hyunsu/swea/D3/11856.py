t = int(input())

for tc in range(1, t+1):
    word = list(input())
    len_word = set(word)
    tmp = 'Yes'

    if len(len_word) != 2:
        print('#{} {}'.format(tc, 'No'))
    else:
        for i in len_word:
            if word.count(i) != 2:
                tmp = 'No'

        print('#{} {}'.format(tc, tmp))


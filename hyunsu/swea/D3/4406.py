t = int(input())
tmp = ['a', 'e', 'i', 'o', 'u']

for tc in range(1, t+1):
    word = input()
    result = ''

    for i in range(len(word)):
        if word[i] not in tmp:
            result += word[i]

    print('#{} {}'.format(tc, result))


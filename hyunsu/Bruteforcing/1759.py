def back(cnt, idx):
    if cnt == l:
        vo, co = 0, 0

        for i in range(l):
            if ans[i] in tmp:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print(''.join(ans))
        return

    for i in range(idx, c):
        ans.append(word[i])
        back(cnt+1, i + 1)
        ans.pop()

l, c = map(int, input().split())
tmp = ['a', 'e', 'i', 'o', 'u']
word = sorted(list(map(str, input().split())))
ans = []

back(0, 0)
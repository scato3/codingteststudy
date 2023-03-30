# def back(cnt, idx):
#     if cnt == l:
#         vo, co = 0, 0
#
#         for i in range(l):
#             if ans[i] in tmp:
#                 vo += 1
#             else:
#                 co += 1
#
#         if vo >= 1 and co >= 2:
#             print(''.join(ans))
#         return
#
#     for i in range(idx, c):
#         ans.append(word[i])
#         back(cnt+1, i + 1)
#         ans.pop()
#
# l, c = map(int, input().split())
# tmp = ['a', 'e', 'i', 'o', 'u']
# word = sorted(list(map(str, input().split())))
# ans = []
#
# back(0, 0)

from itertools import combinations

L, C = map(int, input().split())
alpha = sorted(input().split())
words = combinations(alpha, L)

for word in words:
    cnt_vow = 0
    for i in word:
        if i in "aeiou":
            cnt_vow += 1

    if cnt_vow >= 1 and L - cnt_vow >= 2:
        print(''.join(word))
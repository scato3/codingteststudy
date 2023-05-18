from itertools import combinations

t = int(input())

for tc in range(1, t+1):
    arr = set(list(map(int, input().split())))
    com = combinations(arr, 3)
    ans = []
    for i in com:
        ans.append(sum(i))
    ans.sort(reverse=True)
    ans = list(set(ans))

    print('#{} {}'.format(tc, ans[4]))



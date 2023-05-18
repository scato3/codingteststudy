t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort()
    ans = []

    for i in range(k):
        ans.append(scores.pop())

    print('#{} {}'.format(tc, sum(ans)))
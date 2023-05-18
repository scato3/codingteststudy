t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    print('#{} {}'.format(tc, round((sum(arr) - min(arr) - max(arr)) / 8)))

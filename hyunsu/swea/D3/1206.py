t = 10

for tc in range(1, t+1):
    n = int(input())
    building = list(map(int, input().split()))
    res = 0

    for i in range(2, n-2):
        def1 = building[i] - building[i-1]
        def2 = building[i] - building[i-2]
        def3 = building[i] - building[i+1]
        def4 = building[i] - building[i+2]

        if def1 > 0 and def2 > 0 and def3 > 0 and def4 > 0:
            res += min(def1, def2, def3, def4)

    print('#{} {}'.format(tc, res))
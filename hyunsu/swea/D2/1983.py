rank = ['A+', 'A0', 'A-', 'B+', 'B0' ,'B-', 'C+', 'C0', 'C-', 'D0']

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = []

    for _ in range(n):
        a, b, c = map(int, input().split())
        pts = a * 0.35 + b * 0.45 + c * 0.2
        arr.append(pts)
    tmp = arr[k-1]
    arr.sort(reverse=True)

    tenrank = arr.index(tmp) // (n // 10)
    ans = rank[tenrank]

    print('#{} {}'.format(tc, ans))



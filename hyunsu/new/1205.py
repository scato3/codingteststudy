n, num, p = map(int, input().split())

if n:
    score = list(map(int, input().split()))
    score.append(num)
    score.sort(reverse=True)
    idx = score.index(num) + 1

    if idx > p:
        print(-1)
    elif n == p and score[-1] == num:
        print(-1)
    else:
        print(idx)
else:
    print(1)
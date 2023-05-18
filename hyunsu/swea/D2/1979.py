t = int(input())

for tc in range(1, t+1):
    n, K = map(int, input().split())
    puzzle = []
    for _ in range(n):
        puzzle.append(list(map(int, input().split())))
    result = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == n-1:
                if cnt == K:
                    result += 1
                cnt = 0

        for k in range(n):
            if puzzle[k][i] == 1:
                cnt += 1
            if puzzle[k][i] == 0 or k == n-1:
                if cnt == K:
                    result += 1
                cnt = 0
    print('#{} {}'.format(tc, result))


# 백준 1018 체스판 다시 칠하기 SILVER lV
# https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())
arr = []
cnt = []

for i in range(n):
    arr.append(input())


for a in range(n-7):
    for b in range(m-7):
        w_index = 0
        b_index = 0

        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] == 'B':
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if arr[i][j] == 'B':
                        b_index += 1
                    else:
                        w_index += 1
        cnt.append(w_index)
        cnt.append(b_index)

print(min(cnt))
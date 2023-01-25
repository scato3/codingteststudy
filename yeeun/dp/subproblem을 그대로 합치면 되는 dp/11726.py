#https://www.acmicpc.net/problem/11726

def tile(n):
    tiles=[1,1]

    if 2 <= n:
        for i in range(2, n+1):
            tiles.append(tiles[i-2]+tiles[i-1])

    return tiles[n]

k = int(input())
if k == 0:
    print(0)
else:
    print((tile(k))%10007)
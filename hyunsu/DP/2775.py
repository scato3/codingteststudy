# 2775 부녀회장이 될테야 BRONZE l
# https://www.acmicpc.net/problem/2775

tc = int(input())

for _ in range(tc):
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)]

    for _ in range(floor):
        for i in range(1, num):
            f0[i] += f0[i-1]
    print(f0[-1])
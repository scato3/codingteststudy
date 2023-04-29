'''
https://www.acmicpc.net/problem/20055
컨베이어 벨트 위의 로봇

컨베이어 벨트 길이 N
총 길이 2N

올리는 위치 : 1
내리는 위치 : N

로봇 이동 조건
1. 이동하려는 칸에 로봇이 없어야 함
-> 로봇은 올리는 위치 1번 에만 올리기 가능 / 내리는 위치 N 에 있으면 내림
2. 이동하려는 칸 내구도가 1이상 남아있어야 함
3. 로봇을 올리는 위치에 올리거나 어떤 칸으로 이동시 칸 내구도는 -1
4. 내구도가 0인 칸의 개수 >= k 종료 아니면 1번으로 무한 굴레


n = 3
k = 2
컨베이어 벨트 n
1 2 3
6 5 4

1(로봇투입) 2 3 ..n(로봇 하차).... 2n

로봇
1 2 .. n(로봇 아웃되니까 0)

컨베이어 벨트 a (내구도)
1 2 1
2 1 2

-> 컨베이어 벨트는 2n 회전하지만 로봇은 N에서 아웃하니까 N만큼만 회전
deque.rotate() : 리스트 요소 회전
t = [1,2,3]
t = deque(t)
t.rotate(2)
t => [2,3,1]
'''

from collections import deque

n, k = map(int, input().split())
a = deque(map(int, input().split()))
robots = deque([0] * n)
ans = 0

while True:
    ans += 1
    a.rotate(1)
    robots.rotate(1)
    robots[-1] = 0    # 로봇 하차 하는 부분

    if sum(robots): #로봇 있으면
        for i in range(n-2, -1, -1):
            if robots[i] == 1 and robots[i + 1] == 0 and a[i + 1] >= 1:
                robots[i + 1] = 1 #로봇 이동
                robots[i] = 0 # 현재 칸에는 로봇 없음
                a[i + 1] -= 1 # 내구도는 -1
            robots[-1] = 0
        if robots[0] == 0 and a[0] >= 1:
            robots[0] = 1
            a[0] -= 1
        ans += 1
        if a.count(0) >= k:
            break

print(ans)

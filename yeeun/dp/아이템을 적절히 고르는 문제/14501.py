#https://www.acmicpc.net/problem/14501
#퇴사

import sys
input = sys.stdin.readline
n = int(input())

schedule = [
    list(map(int,input().split()))
    for _ in range(n)
]

#p[i] i번째 날까지 최대 이익
p = [0] * (n+1)

#T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]

'''

 	    1일	2일	3일	4일	5일	6일	7일
Period	3	5	1	1	2	4	2
Value	10	20	10	20	15	40	200
'''

for day in range(n-1, -1, -1): #5,4,3 ... 0

    period = schedule[day][0]
    value = schedule[day][1]
    # 현재 날짜 + 상담 시행 기간이 퇴사 날짜 전이라면
    if day + period <= n:
        #p[day] = day날에 상담을 하기 or 상담 건너뛰기
        #p[5] = max(p[7]+15 , p[6])
        p[day] = max(p[day+period] + value , p[day+1])
    # 현재 날짜에 상담 불가 할 때
    else:
        p[day] = p[day+1]
print(p[0])
#[45, 44, 42, 39, 35, 30, 24, 17, 9, 0, 0]
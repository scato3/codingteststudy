# 300162
# 전자레인지

"""
버튼 A B C가 달린 전자레인지가 있다.
버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초이다. 
T초를 위한 최소버튼 조작의 A B C 횟수를 첫 줄에 차례대로 출력해야 한다.
만일 제시된 3개의 버튼으로 T초를 맞출 수 없으면 음수 -1을 첫 줄에 출력해야 한다. 

입력
100

출력
0 1 4
"""
import sys
input = sys.stdin.readline

t = int(input())
btns = [300, 60, 10]
cnt_300 = 0
cnt_60 = 0
cnt_10 = 0
if t > 0:
    cnt_300 += t//300
    t = t % 300
    cnt_60 += t//60
    t = t % 60
    cnt_10 += t//10
    t = t % 10


if (t != 0):
    print(-1)
else:
    print(f"{cnt_300} {cnt_60} {cnt_10}")

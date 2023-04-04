'''
https://www.acmicpc.net/problem/15810

풍선을 담당하는 N명의 스태프
각 스태프가 풍선 하나를 만드는 시간(분) Ai를 알고 있을 때, 풍선 M개를 만들기 위해서 최소 몇 분이 걸릴까?

스태프의 수 N과 풍선의 개수 M이 입력된다. (1 ≤ N, M ≤ 1 000 000)
풍선 하나 만드는 데 걸리는 시간 Ai는 1 000 000 이하의 자연수

접근 방법
: 시간을 탐색하라!
1. 임의의 시간을 정하고
2. 해당 시간동안 만들 수 있는 풍선의 수 temp_count
3. temp_count와 M비교해보고

'''
import sys

input = sys.stdin.readline
n,m=map(int,input().split())
times = list(map(int,input().split()))
times.sort()

start = times[0]
end = 1000000*1000000
result = 1000000*1000000 #최솟값을 구하는 문제이니만큼 ! 꼭 초기값을 제일 크게 세팅해놓고 비교해서 작은 값을 남기도록 하자!

while start <= end:
    temp_time = (start+end)//2
    #sum은 iterable자료형인 리스트,튜플,딕셔너리를 인자로 받음 따라서 밑의 코드는 에러
    #temp_count = sum(min(temp_time // x) for x in times) 에러 코드
    temp_count = sum([temp_time // x for x in times])
    if m == 0:
        print(0)
    else:

        if temp_count >= m:
            result = min(result,temp_time)
            end = temp_time - 1
        else:
            start = temp_time + 1
print(result)
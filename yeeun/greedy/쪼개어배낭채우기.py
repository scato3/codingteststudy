# code_tree
# 쪼개어 배낭 채우기
"""
보석방에는 n개의 보석이 있고, 도둑 가방의 크기는 m.
보석은 종류별로 단 하나씩만 있으며 각 보석을 원하는 만큼 쪼개어 담는 것이 가능합니다.
도둑 가방 크기의 정보와 보석의 정보가 주어졌을 때, 얻을 수 있는 최대 가치를 구하는 프로그램을 작성해보세요.

입력 형식
첫째 줄: N과 M이 공백을 사이에 두고 주어집니다
두 번째 줄 부터: N개의 줄에 걸쳐 보석의 정보 (w 보석 무게, v 보석 가치) 가 공백을 사이에 두고 주어집니다

입력 예시
3 7
5 8
3 6
4 4

출력 예시
12.400
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = 0  # 가방에 들어가는 가치

# 보석 무게, 가치 2차 배열 입력 받기
arr = [
    tuple(map(int, input().split()))
    for i in range(n)
]

# [무게당 가치, 개수]
# [3, 6]의 경우 [2, 3] 1무게에 2의 가치가 있는 보석이 3개 까지 넣을 수 있음

perOneWeight = [
    [0, 0]
    for i in range(n)
]


for i in range(n):
    perOneWeight[i][0] = (arr[i][1]/arr[i][0])
    perOneWeight[i][1] = arr[i][0]
# 가치/무게 가 큰 순서대로 내림차순 정렬
perOneWeight.sort(reverse=True)


for i in range(n):  # 3
    # perOne[0][1] perOne[0][1] perOne[0][1]
    for j in range(perOneWeight[i][1]):
        if m > 0:
            result += perOneWeight[i][0]
            m -= 1


print(f"{result:.3f}")

# ver 2
n, m = tuple(map(int, input().split()))
jewels = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
ans = 0

# 가치/무게 내림차순 정렬
jewels.sort(key=lambda x: -x[1]/x[0])

for w, v in jewels:
    # 현재 보석을 다 담을 수 있다면 담기
    if m >= w:
        m -= w
        ans += v
    # 현재 보석을 온전히 담을 수 없다면 쪼개어 채우고 종료
    else:
        ans += m/w*v
        break
print(f"{ans:.3f}")

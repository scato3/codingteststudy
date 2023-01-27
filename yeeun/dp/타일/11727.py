#https://www.acmicpc.net/problem/11727
# 타일링2
'''
실패: f(n)을 5까지 하나하나 구해서 규칙성을 찾아보려 했는데 f(8)이 171이 라니 ... 이건 숫자를 구해서 규칙성을 찾으면 안된다.
처음부터 점화식으로 구하려 했어야 했다.

접근법:
DP[n] = 2*n 타일을 채울 수 있는 경우의 수

2*n을 채우기 위해선
1) 2*(n-1) 에다가 2*1 타일을 더하기
2) 2*(n-2) 에다가 2*2 타일을 더하기
3) 2*(n-2) 에다가 1*2 1*2 타일을 더하기

DP[n] = DP[n-1] + 2*DP[n-2]
'''

#NameError 났다 ... 왜 ...???
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
#sys.setrecursionlimit(10000)를 뺴니 정답이 나왔다.
def Titles(n):
    DP = [0, 1,3]

    if n>2:
        for i in range(3,n+1):
            DP.append(DP[i-1] + 2*DP[i-2])

    return DP[n]
n = int(input())

print(Titles(n) % 10007)
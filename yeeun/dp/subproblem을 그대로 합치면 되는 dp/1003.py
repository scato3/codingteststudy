#https://www.acmicpc.net/problem/1003
#피보나치 함수


#실패 방법 ) f(0), f(1)을 리턴 할 때 cnt 더하기 -> 시간초과 ...
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

def fibo(n):

    cnt0 = [1,0]
    cnt1 = [0,1]
    if n >= 2:
        for i in range(2, n+1):
            cnt0.append(cnt0[i-2]+cnt0[i-1])
            cnt1.append(cnt1[i-2]+cnt1[i-1])
    return (cnt0, cnt1)

n = int(input())
cases=[
    int(input())
    for _ in range(n)
]

for n in (cases):
    cnt0 , cnt1 = fibo(n)
    print(cnt0[n], cnt1[n])
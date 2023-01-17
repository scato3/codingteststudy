#https://www.acmicpc.net/problem/2748
#피보나치수2

'''
F0 = 0
F1 = 1
Fn = Fn-1 + Fn-2 (n ≥ 2)
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
'''

'''
dp 익히기
1. 큰 문제를 작은 문제로 나눈다. : Fn = Fn-1 + Fn-2
2. 작은 문제를 푼다  : Fn-1 + Fn-2 
3. 재귀
'''
n = int(input())
fibo_num = 0
arr=[]
for i in range(n+1):
    arr.append(i)

def fibo(n):

    for i in range(2,n+1):
        arr[i] = arr[i-2] + arr[i-1]
    return arr[-1]

print(fibo(n))

#다른 초 간단 코드

'''
fibonacci=[]
num = 0
for i in range(n+1):
    if i == 0:
        num = 0
    elif i <= 2 :
        num = 1
    else:
        num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(num)
print(fibonacci[-1])
'''


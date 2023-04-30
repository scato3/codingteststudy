'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PhcWaAKIDFAUq&categoryId=AV5PhcWaAKIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2
정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
'''

n = int(input())
for i in range(1, n+1):
    if n == i:
        print(i)
    else:
        if n%i == 0:
            print(i,end=" ")

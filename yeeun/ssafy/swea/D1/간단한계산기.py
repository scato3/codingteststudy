'''
두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjsYKAMIDFAUq&categoryId=AV5PjsYKAMIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2

'''
a, b = map(int,input().split())
print(a+b, a-b, a*b, a//b, sep="\n")


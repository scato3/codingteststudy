'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2
가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.
가위 < 바위 1 < 2
바위 < 보   2 < 3
보 < 가위   3 < 1
'''
A, B = map(int,input().split())
if A > B : # 3>2 2>1 3>1
    if A -B == 1:
        print('A')
    else:
        print('B')
else:
    if B-A == 1:
        print('B')
    else:
        print('A')
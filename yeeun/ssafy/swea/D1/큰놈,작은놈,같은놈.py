'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1
2개의 수를 입력 받고 비교해서 <, >, = 표기해라
'''

T = int(input())

for test_case in range(1, T+1):
    a, b = map(int,input().split())
    if a > b:
        print(f"#{test_case} >")
    elif a == b:
        print(f"#{test_case} =")
    else:
        print(f"#{test_case} <")
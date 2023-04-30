'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV2gbY0qAAQBBAS0&categoryId=AV2gbY0qAAQBBAS0&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=2

주어진 숫자부터 0까지 순서대로 찍어보세요
'''

n = int(input())
if n == 0:
    print(n)
else:
    for i in range(n, 0, -1):
        print(i,end=' ')
    print(0)
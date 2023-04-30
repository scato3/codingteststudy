'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

10개의 수를 입력 받고, 그 중 가장 큰 수 출력하시오
'''

import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, 1+T):
    arr = list(map(int,input().split()))
    tmp = arr[0]
    for i in arr:
        if i > tmp:
            tmp = i
    print("#",test_case," ",tmp,sep="")
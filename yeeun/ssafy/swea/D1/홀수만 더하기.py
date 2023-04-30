'''

https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=30&pageIndex=1
10개의 수를 입력받아 홀수만 더한 값을 출력하시오
'''

n = int(input())
for test_case in range(1,1+n):
    arr = list(map(int,input().split()))
    ans = 0
    for i in arr:
        if i % 2 == 1:
            ans+=i
    print("#",test_case,sep="",end=" ")
    print(ans)
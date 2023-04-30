'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1
10개의 수를 이벽 받아 평균갑 출력
소수점 첫 번쨰 자리에서 반올림 출력
'''
T = int(input())

for test_case in range(1, 1+T):
    arr = list(map(int, input().split()))
    average = round(sum(arr) / 10)
    print(f"#{test_case} {average}")
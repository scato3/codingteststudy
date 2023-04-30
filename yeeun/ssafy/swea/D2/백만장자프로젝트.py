'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

다음과 같은 조건 하에 사재기해서 최대 이득을 얻게 하자
1. 하루에 0개, 1개만 구매가능
2. 판매는 얼마든지 가능

 1 2 3
 2개를 3원에 구입 -> 3쨰날 2개 6원에 팔면 -> 3원 이득

3 5 9
3 + 5 = 8
18 -8 = 10

1 1 3 1 2
주머니에 있는 돈 :
사기 1 + 1 = -2 / 팔기 6 - 2 = 4 / 사기 4 -1 = 3/ 팔기 3 + 2 = 5
-1-1+ 6 + -1 + 2

10 7 6

'''
# import sys
# sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    profit = 0
    All_profit = 0
    for i in range(len(arr)-1):

        if arr[i] > arr[i+1]:
            #파는 날
            All_profit = profit + (arr[i]*cnt)
            cnt = 0
            profit = 0
        else:
            #사는 날
            profit -= arr[i]
            cnt += 1
            if i == len(arr)-2:
                All_profit += profit + (arr[-1]*cnt)

    print(f"#{test_case} {All_profit}")
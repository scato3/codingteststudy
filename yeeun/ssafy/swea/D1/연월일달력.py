'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1
yyyymmdd가 주어짐 -> yyyy/mm/dd로 출력
유효하지 않으면 -1
유효 조건
1. 달의 범위 1~12
2. 일의 범위 ... 생략

'''
d_range=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for t in range(1, T+1):
    date = list(input())
    mm = int(date[4]+date[5])
    if 12 >= mm >= 1:
        dd = int(date[-2]+date[-1])
        if 0 <= dd <= d_range[mm]:
            print(f"#{t} {date[0] + date[1] + date[2] + date[3]}/{date[4]+date[5]}/{date[-2]+date[-1]}")
        else:
            print("#",t,' ',-1,sep="")
    else:
        print("#",t,' ',-1,sep="")
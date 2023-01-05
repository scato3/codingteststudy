# https://www.acmicpc.net/problem/2839
# 설탕배달
"""
상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 
설탕 봉지는 3kg 봉지, 5kg 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.

입력 
N
출력
상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

"""

n = int(input())
cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += n//5
        print(cnt)
        break
    n -= 3
    cnt += 1
else:
    print(-1)
"""
while n > 0:
    if (n % 5 == 0):
        cnt += n // 5
        n = 0
        print(cnt)

        break
    elif(n % 3 == 0):
        cnt += n//3
        n = 0
        print(cnt)

        break
    else:
        a = n//5
        b = n//3

        if(n-(5*(n//5)) - (3*((n % 5)//3)) == 0):
            cnt += n//5
            cnt += (n % 5)//3
            print(cnt)

            break
        elif(n-(3*(n//3)) - (5*((n % 3)//5)) == 0):
            cnt += n//3
            cnt += (n % 3)//5
            print(cnt)

            break
        else:
            print(-1)
            break
"""

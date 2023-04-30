'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QPRjqA10DFAUq&categoryId=AV5QPRjqA10DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1
자연수의 각 자릿수를 합하여 출력하시오

9999
1000*9
100*9
10*9
1*9

'''


'''
n = int(input())
ans = 0
for i in range(3,-1,-1):
    num = (n//(10**i))
    n -= num*(10**i)
    ans+=num
print(ans)
'''
n = input()
ans = 0
n = list(n)
for i in n:
    ans+=int(i)
print(ans)
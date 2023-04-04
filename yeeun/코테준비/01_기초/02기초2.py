# 중첩 반복문, 문자열, 내장함수, 리스트, 2차원 리스트, 람다함수
#------------------------------------------------------
# 1. 중첩 반복문
'''
0 1 2 3
0 1 2 3
0 1 2 3
출력해라
'''
for i in range(3):
    for j in range(4):
        print(j, end=' ')
    print() #줄바꿈

#--------------------

for i in range(5):
    print('i:', i, sep='', end=' ')
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print()
'''
i:0 j:0 j:1 j:2 j:3 j:4
i:1 j:0 j:1 j:2 j:3 j:4
i:2 j:0 j:1 j:2 j:3 j:4
i:3 j:0 j:1 j:2 j:3 j:4
'''

for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()
'''
* * * * *
* * * * *
...
'''

for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()
'''
* 
* * 
* * *
* * * *
* * * * *
'''

#위의 별 피라미드를 상하반전한 케이스를 코딩해라

#틀림
for i in range(5,0, -1):
    for j in range(i-1):
        print('*',end=' ')
    print()
#맞음
for i in range(5): #다섯바퀴 돈다
    for j in range(5-i):
        print('*',end=' ')
    print()

#------------------------------------------
# 2. 문자열과 내장함수

#대문자 upper() 소문자 lower()
str = 'Hello'
print(str.upper())
print(str.lower())

#문자열.find('문자') 해당 문자가 '처음으로'발견되는 인덱스 번호
#문자열.count('문자') 해당 문자가 문자열에 몇 개 있는 가
tmp = str.upper()
tmp.find('L') # 2

msg = "It is time" #공백도 리스트에 들어감
tmp.find('i') #3
tmp.find('i') #2
len(tmp) # 10 1부터 셈.공백포함
#문자열[:2] -> 0~1까지 추출
str[:2]  #He
#문자열[3:5] -> 3~4 까지 추출

for s in str:
    print(s,end=' ')
#H e l l o

for s in str:
    if s.isupper(): #대문자라면 참
        print(s, end=' ')
#H

for m in msg:
    if m.isalpha(): #알파벳이라면 참 => 공백은 X
        print(m, end='')
#Itistime


# ord('문자') 문자의 아스키 넘버 리턴
tmp = 'AZ'
for x in tmp:
    print(ord(x))
#65
#90

# chr('숫자') 숫자의 아스키 문자 리턴
tmp = 65
print(chr(tmp)) #A








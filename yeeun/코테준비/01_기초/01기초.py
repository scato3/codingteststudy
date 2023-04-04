#------출력
# sep
a, b, c = 1, 2, 3
# sep - 줄바꿈
print(a, b, c, sep='\n')

# end (print에 있는 기본 줄바꿈을 없애줌)
print(a, end= ' ')
print(b, end= ' ')


#------조건문 if
x = 90
if x >= 90:
    print('clear 1')
if x >= 80:
    print('clear 2')
#clear1, clear2 출력


#------- 반복문 for
a = range(10)
#a= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range (10, 0, -2): #10부터 1까지
    print(i) # 10 8 6 4 2

for i in range(1, 11):
    if i%2 == 0:
        continue # 이 이하에 있는 코드는 다 무시
    print(i)
# 1 3 5 7 9

'''
for-else : 
* for문에서 break가 걸리면 else도 무시하고 빠져나옴
* for문이 다 진행되면 else문이 진행됨
'''
for i in range(1, 11):
    print(i,end=' ')
    if i == 5:
        break
else:
    print(11)
#1 2 3 4 5

for i in range(1, 11):
    print(i,end=' ')
    if i >= 11:
        break
else:
    print(11)
#1 2 3 4 5 6 7 8 9 10 11

# --------반복문 while
i = 1
while i <= 10:
    print(i)
    i+=1
while True:
    print(i)
    if i == 10:
        break
    i+= 1

#----------- 반복문 문제 풀이
#1) 1부터 N까지 홀수
N = int(input())
for i in range(N+1):
    if i%2 ==0:
        continue
    print(i)
#2) 1부터 N까지 합
sum = 0
for i in range(N+1):
    sum += i
print(sum)

#3) N의 약수 출력 (N으로 나누어 떨어지는 수)

for i in range(N+1):
    if N%i == 0:
        print(i)


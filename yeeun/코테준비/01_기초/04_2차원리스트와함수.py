a = [0] * 3 #[0, 0, 0]
b = [[0]*3
     for _ in range(2)] #[ [0,0,0], [0,0,0] ]

for x in b:
    print(x)

for x in b:
    for y in x:
        print(y, end=" ")
    print()
'''
for x in b:
    print(x)
일차원 리스트 단위로 출력
[0,0,0]
[0,0,0]

for x in b:
    for y in x:
        print(y, end=" ")
    print()
값들만 나오게 하고 싶을 때 
0 0 0
0 0 0
'''

#소수 출력 함수
def isPrime(x):
    for i in range(x):
        if x%i == 0:
            return False

    return True
#람다 함수
def plus_one(x):
    return x+1
print(plus_one(1))

#lambda (매개변수) : (함수내용)
#람다함수는 리턴값을 제공하기 때문에 변수에 할당하여 사용해야 함
plus_two = lambda x: x+2

#내장함수의 인자로 사용할때 주로 람다를 사용

#map(함수, 자료) -> 자료를 함수해라
a=[1,2,3]
list(map(plus_one,a)) #2 3 4
list(map(lambda x: x+1, a)) # 2 3 4


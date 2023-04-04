#리스트 내장함수
'''
하이라이트
'''
a = [1, 36, 52]
for index, value in enumerate(a):
    print(index,value)

# all -> 모든 원소가 조건을 만족할 때만 T 반환
all(60 > x for x in a) # 만약 a 리스트 원소 모두 60보다 작으면 True반환
# any -> 모든 원소가 조건을 불만족할 때만 F 반환
any(60 > x for x in a) # a리스트 중에 하나라도 60보다 작은 게 있다면
#--------start---------------------------------
import random as r

#빈리스트 만드는 2가지 방법
a=[]
b=list()
a.clear()
#리스트 만드는 다양한 방법들
c = list(range(1,6)) #[1, 2, 3, 4, 5]

d = [1,2,3]
print(c+d) #[1,2,3,4,5,1,2,3]

#추가함수 append(숫자), insert(인덱스,숫자)
d.append(6) # d=[1,2,3,6]
d.insert(1,7) # d=[1,7,2,3,6]

#삭제
#리스트.pop(), pop(인덱스)
# d=[1,7,2,3,6]
d.pop() #d=[1,7,2,3]
d.pop(0) #d=[7,2,3]

#리스트.remove(숫자)
d.remove(2) # d=[1,7,3]

#리스트.idex(숫자) 숫자의 인덱스
# d=[1,7,3]
d.index(3) #2

e = list(range(1,11))
#sum, max, min
sum(e)
max(e) #e리스트 중 가장 큰 값
min(e)

#shuffle
r.shuffle(e) #e 리스트를 randomly하게 섞어라
print(e) #랜던하게 섞인 요소들

#정렬 sort() 
e.sort() # 1 2 3 ...
e.sort(reverse=True) #내림차순 10 9 8 ...
e.clear() #빈리스트 리스트 초기화


#slice 슬라이스
a= [23, 12, 36, 53, 19]

#a[:3] 0 1 2 자르기 3전까지 자름!
print(a[:3]) # [23, 12, 36]
print(a[1:3]) #[12, 36]

# enumerate 인덱스와 값 모두 출력
for x in enumerate(a):
    print(x)
'''
튜플로 출력됨 
(0, 23)
(1, 12)
(2, 36)
...
'''
print()

for index, value in enumerate(a):
    print(index,value)
#tuple 튜플
b = (1, 2, 3, 4, 5)
print(b[0]) #5
b[0] = 7 #에러!!!!! 튜플은 값 변경 불가

if all(60 > x for x in a):
    print('all of the element is under 60')
else:
    print('some element is over 60')

if any(60 > x for x in a):
    print('some of the element is under 60')
else:
    print('all of element is over 60')
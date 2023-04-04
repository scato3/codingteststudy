'''
https://www.acmicpc.net/problem/19637
** 조건 범위가 10억을 넘는다면! 이분 탐색을 의심해봐라!!
** 그냥 for문을 돌리면 10만 x 10만 = 100억 연산이 걸린다


WEAK 10000 ( <= 10000)
NORMAL 100,000 (10000 < <= 100,000)
STRONG 1,000,000 (100,000 < <= 1,000,000)

칭호는 전투력 상한값의 비내림차순 (= 오름차순) 으로 주어진다.

시 간 초 과 ... !!!!!! ㅠㅠ
'''


import sys
input = sys.stdin.readline
n,test_n = map(int, input().split())

systems = []
for i in range(n):
    sys = input().split()
    sys[1]=int(sys[1])
    systems.append(sys)
def search(target,systems):
    start = 0
    end = n-1
    while start <= end:
        point = (start+end) //2
        if target > systems[point][1]:
            start = point + 1
        else:
            end = point-1
    return end+1

for i in range(test_n):
    target = int(input())
    print(systems[search((target),systems)][0])

'''
n,test_n = map(int, input().split())
def search(target,numbers):
    start = 0
    end = n-1
    # if start > end :
    #     return None
    while start <= end:
        point = (start+end) //2
        if target > numbers[point]:
            start = point + 1
        else:
            end = point-1
    return end+1



titles=[]
numbers=[]
for i in range(n):
    title, number = input().split()
    number = int(number)
    if number in numbers:
        n-=1
        continue
    numbers.append(number)
    titles.append(title)

for i in range(test_n):
    index = search(int(input()), numbers)
    print(titles[index])

'''
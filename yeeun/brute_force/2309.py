#https://www.acmicpc.net/problem/2309
#일곱 난쟁이
'''
난쟁이 9명 중 일곱 난쟁이 7명을 찾아라
7명의 키 합은 100이다.
'''

import itertools
heights = [
    int(input())
    for _ in range(9)
]

combie = list(itertools.combinations(heights,7))

for i in combie:
    if sum(i) == 100:
        result = list(i)

result.sort()

for el in result:
    print(el)
'''
일곱난쟁이

9명 중 7명을 찾아내라
7명의 키 합 = 100
'''

heights = []
for i in range(9):
    heights.append(int(input()))
SUM = sum(heights)
BREAK = False
for i in range(9):
    for j in range(i+1, 9):
        if SUM - (heights[i] + heights[j]) == 100:
            tmp1 = heights[i]
            tmp2 = heights[j]
            heights.remove(tmp1)
            heights.remove(tmp2)
            # heights.remove(heights[i])
            # heights.remove(heights[j])

            BREAK = True
            break
    if BREAK == True:
        break

heights.sort()
for h in heights:
    print (h)
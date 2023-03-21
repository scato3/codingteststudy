# code_tree
# 연속 부분 합의 최댓값 구하기

"""
다음과 같이 8개의 숫자가 주어졌을 때
특정 구간을 잡아 그 구간 내에 있는 숫자의 합이 최대가 되도록 해보세요.
[4, 3, -6, 9, -15, 1, 3, -2]
요런 유형

진짜 문제
n개의 정수가 입력으로 주어지고, 이 중 연속한 부분 수열에 속한 원소들의 합이 최대가 될 때의 값을 출력하는 코드를 작성해보세요.
(단, 부분 수열은 최소 한 개 이상의 원소를 포함합니다.)

입력:
7
4 -1 2 -19 3 6 9
출력:
18

-> 왼쪽부터 차례대로 더하고 저장 반복 -> 더한 수가 음수가 될 경우 멈추고 저장 -> 합을 초기화 한 뒤 그 다음 수부터 다시 더하기 시작한다. 

"""

import sys
n = int(input())
nums = list(map(int, input().split()))  # 4 2 -1 -5 3
# 수열의 합 리스트
ans = []
ans.append(nums[n-1])  # ans=[3]
# 현재 수열의 합
result = nums[0]  # r = 4


for i in range(1, n):
    result += nums[i]  # r = 6
    if (result < 0):
        ans.append(result - nums[i])
        if (i == n-1):
            break
        result = 0
    ans.append(result)  # ans=[6, ]


result = ans[0]

for i in ans:
    result = max(result, i)
print(result)

# ---------------------------------------
# ver2

INT_MIN = -sys.maxsize

n = int(input())
arr = [0] + list(map(int, input().split()))

# 초기값을 정수의 제일 낮은 수로 잡기 (max로 비교하면서 합 중 제일 큰 수를 찾아야 하니까)
ans = INT_MIN

# 현재 수열의 합
sum_of_nums = 0

for i in range(1, n+1):
    # 현재 수열의 합이 0볻 작으면 새로운 부분 수열 만들어 줌
    if sum_of_nums < 0:
        sum_of_nums = arr[i]
    # 그렇지 않다면 기존 연속 부분 순열에 현재 원소 추가하기
    else:
        sum_of_nums += arr[i]

    ans = max(ans, sum_of_nums)
print(ans)

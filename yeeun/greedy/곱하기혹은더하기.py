# 이것이 취업을 위한 코딩테스트다.
# 곱하기 혹은 더하기
"""
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, + 보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 ((((0 + 2) x 9) x 8) x 4) = 576입니다.
또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

입력 조건
첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 20)

출력 조건
첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

입력 예시 1
02984

출력 예시 1
576
"""
number = list(input())
arr_number = [int(i) for i in number]


for i in range(len(arr_number)-1):
    addition = arr_number[i] + arr_number[i+1]
    multiply = arr_number[i] * arr_number[i+1]

    if (addition > multiply):
        arr_number[i+1] = addition
    else:
        arr_number[i+1] = multiply
print(arr_number[-1])

# 책 풀이
# 0,1 인 경우에는 곱셈 < 덧셈이 더 효율. 이외에는 다 곱셈이 효율

data = input()

# 첫 번째 문자를 숫자로 변경
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    # num, result 둘 중 하나가 0혹은1이라면 덧셈, 그외에는 곱셈
    if num <= 1 or result <= 1:
        result += num
    else:
        result += num

print(result)

'''
https://www.acmicpc.net/problem/1300

배열 A : 크기 NxN
  1 2 3
1 1 2 3
2 2 4 6
3 3 6 9
B = 1 2 2 3 3 4 6 6 9
k = 6
b[k] = 4



A[i][j] = i*j
-> 일차원 배열에 넣고 오름차순 한 뒤 -> K번쨰 수 구하기

메모리 초과 ... 두둥 ....

접근법
: A보다 작은 숫자가 몇 개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다!!
B[k] 이하인 숫자들의 개수 +1 = k

1. 대충 어떤 숫자(value)를 정한다.
    1-1. 숫자는 (제일 작은 수 start + 제일 큰 수 end) 의 중간 값으로 정한다.
2. 그 숫자의 index를 구한다.
3. 해당 index가 K와 동일한 지, K보다 큰 지, K보다 작은 지 확인 한다.
    3-1. 만약 k랑 같거나 크다면 ->
        value보다 B[k]는 작은 숫자 이기에 end = value -1
        (K랑 같을 경우도 포함되므로) 결과값에 value 저장
    3-2. 만약 K보다 작으면 ->
        value값이 B[k]보다 작기에 start = value+1

* 오름차순 정렬된 배열에서 index구하는 방법 = 어떤 숫자 이하인 숫자의 개수 구하는 법
(단, index를 1부터 시작한다고 했을 떄)
    sum(min(value//i,N) for i in range(1,N+1))
ex) 4 X 4 이차배열 i*j를 원소로하는  B에서 10보다 작거나 같은 수의 index (10이하의 숫자 개수)
min(10 // 1, 4) +
min(10 // 2, 4) +
min(10 // 3, 4) +
min(10 // 4, 4)
= 13
B = [1, 2, 2, 3, 3, 4, 4, 4, 6, 6, 8, 8, 9, 12, 12, 16]
10이하의 숫자의 개수 = 13
10보다 작거나 같은 수의 개수 = 13
B[13] = 9 (1부터 인덱스 시작일 때)

'''


n = int(input())
k = int(input())

def b_search(n,k):
    start = 1
    end = n*n
    result = 0
    while start <= end:
        temp_value = (start + end) // 2

        temp_idx = sum(min(temp_value//i, n) for i in range(1,n+1))
        if temp_idx >= k:
            result = temp_value
            end = temp_value -1
        else:
            start = temp_value +1
    return result
print(b_search(n,k))



'''
배열로 풀면 메모리 초과됨
n = int(input())
k = int(input())
A = [[((i+1)*(j+1)) for j in range(n)] for i in range(n)]
arr = []
for i in range(n):
    for j in range(n):
        arr.append(A[i][j])
arr.sort()

print(arr[k])
'''
'''
메모리 초과됨 재귀 때문에 그런듯
def b_search(start, end, arr, k):
    # if start > end:
    #     return None
    point = (start + end) // 2
    if arr[point] == arr[k]:
        return point
    elif arr[point] > arr[k]:
        return b_search(start, point-1, arr,k)
    else:
        return b_search(point+1,end,arr,k)

print(b_search(0, len(arr)-1, arr, k))
'''


#https://www.acmicpc.net/problem/1065
#한수
'''
한수 : 정수 x의 각 자리가 등차수열을 이룸
등차수열 : 연속된 두 개의 수의 차이가 일정한 수열
1<=한수<=N 인 한수 개수 출력
'''

N = int(input())
hansu = 0


for i in range(1,N+1):
    if i<100:
        hansu += 1
    else:
        nums = list(map(int, str(i)))
        if (nums[0] - nums[1] == nums[1] - nums[2]): hansu+=1


print(hansu)
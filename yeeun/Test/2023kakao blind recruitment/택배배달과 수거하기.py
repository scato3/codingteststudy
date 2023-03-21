'''
n개의 집 택배 배달 & 수거
배달할 택배: 물류창고에 보관
i번째 집은 물류창고에서 거리 i만큼 떨어져 있음


cap : 트럭에 실을 수 있는 최대 재활용 택배 상자 수

ex) cap : 4
배달   1    0   3   1   2
수거   0    3   0   4   0

트럭3               2   0
수거                4

배달   1    0   3   0   0
수거   0    3   0   0   0

트럭4  3        0
수거        3
'''
from collections import deque
cap = 4
n = 5
# deliveries =[0,0,0,1,2]
deliveries =[1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]



def delivery(cap, n, deliveries, pickups):
    ans = 0
    #뒤에서부터 보면서 0인 건 지우기
    while deliveries or pickups:
        #deliveries에서 뒤가 0인 건 지우기

        for i in reversed(range(len(deliveries))):
            if(deliveries[i] == 0):
                del deliveries[i]
            else:
                break
        # pickups 에서 뒤가 0인 건 지우기
        for i in reversed(range(len(pickups))):
            if (pickups[i] == 0):
                del pickups[i]
            else:
                break
        ans += 2*(max(len(pickups), len(deliveries)))

        #박스를 배달하는 경우
        #cap 초기화
        d_cap = cap
        for d in reversed(range(len(deliveries))):
            #배달 미완료 : 배달해야하는 박스 숫자 > cap
            if deliveries[d] > d_cap:
                deliveries[d] -= d_cap
                break
            else:
                #배달 완료
                d_cap -= deliveries[d]
                deliveries[d] = 0
        # 박스를 픽업하는 경우
        # cap 초기화
        p_cap = cap
        for p in reversed(range(len(pickups))):
            # 픽업 미완료 : 픽업해야하는 박스 숫자 > cap
            if pickups[p] > p_cap:
                pickups[p] -= p_cap
                break
            else:
                # 픽업 완료
                p_cap -= pickups[p]
                pickups[p] = 0
    print(ans)
    return (ans)



(delivery(cap, n, deliveries, pickups))
# arr1=[0,0,1,1,0,0,0]
# while arr1 and arr1[-1]==0 :
#     del arr1[-1]
# print(arr1)

# arr2 = [0,1,1,0,0]
# for i in reversed(range(n)):
#
#     if (arr2[i] == 0):
#         print('first', arr2[i])
#         del arr2[-1]
#     else: continue
# arr2 = [0,1,1,0,0]
# while arr2 and arr2[-1] == 0:
#     print (arr2[-1])
#     del arr2[-1]
#
# for i in reversed(range(n)):
#     print (pickups[i])

# while deliveries and deliveries[-1] == 0:
#     del deliveries[-1]
# while pickups and pickups[-1] == 0:
#     del pickups[-1]
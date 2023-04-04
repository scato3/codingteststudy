def solution(C):
    addresses = []
    idx = 0
    if C[0][0] == "PUSH":
        addresses.append(C[0][1])
    print("initial", addresses)
    for i in range(1, len(C)):
        if C[i][0] == "PUSH":
            idx += 1
            addresses.insert(idx, C[i][1])
            print("JUSST PUSH", addresses)
            if idx != len(addresses) - 1:
                print("pre PUSH", addresses)
                del addresses[idx+1:]
                print("later PUSH", addresses)

        elif C[i][0] == "BACK":
            if idx != 0:
                idx -= 1
            print("back", addresses, "idx", idx)
        elif C[i][0] == "NEXT":
            # print("next", addresses)
            if idx == len(addresses) - 1:
                idx += 1
            print("next", addresses, "idx", idx)
    # return addresses[idx]
    return addresses, idx

C= [["PUSH","www.domain1.com"],["PUSH","www.domain2.com"],["PUSH","www.domain3.com"],["BACK","1"],["BACK","1"],["PUSH","www.domain4.com"]]
print(solution(C))

#개발 능력 구현 검사
#복기
# 마지막 단계는 이전에 방문한 웹사이트 모두 리턴. 만약 반복되는 게 있다면 가장 최근에 방문한 곳만 남기고 중복은 지우기
# 첫 번째 단계는 back은 -1해서 웹사이트 next는 +1해서 웹사이트 전송
#웹페이지 방문 로직 구현
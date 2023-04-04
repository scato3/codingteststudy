'''
https://www.acmicpc.net/problem/5014

스타트 링크에 도착하려고 함.

사무실 : F층 높이
강호 위치: S층
스타트링크 : G층

버튼: U-> U층 위로 / D -> D층 아래
강호가 G층에 도착하려면, 버튼(업 or 다운)을 적어도 몇 번 눌러야 하는지 구하는 프로그램
만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.

'''


from collections import deque


def bfs(s):
    queue = deque()
    queue.append(s) #시작을 큐에 넣어서 탐색
    visited[s] = 1 #먼저 시작점 방문 표시

    updown = [u, -d]
    while queue:
        a = queue.popleft()

        # 도착했다면
        if a == g:
            return visited[a] - 1

        for i in updown:
            if 0 < a + i < f + 1:
                if visited[a + i]:
                    continue
                queue.append(a + i)
                visited[a + i] = visited[a] + 1

    return "use the stairs"


f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)
print(bfs(s))
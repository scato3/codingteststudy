# GREEDY

<이것이 취업을 위한 코딩테스트다 with 파이썬>을 토대로 작성하였습니다.

- 눈 앞의 선택에서 최적의 상황만 탐하는 방법. 최종 결과가 최적의 해가 될 순 없다. -> 탐욕법으로 얻은 해가 최적의 해가 되는 상황을 추론할 수 있어야 풀리도록 출제됨

## 대표문제

📂거스름 돈 문제

- 큰 단위의 화폐부터 거슬러주는 것이 왜 최적의 해를 보장하는 것인가? <br> 가지고 있는 동전 중 가장 큰 단위가 항상 작은 단위의 배수이므로. <br>
  -> 800원 거슬러 줘야하는 상황. 큰 단위가 작은 단위의 배수가 아닐 때) 단위가 500 / 400 / 100원이라면 400\*2 가 최적의 해가 됨

  <details>
  <summary>유형 문제</summary> </br>
  <div markdown="1">
    11047
  </div>
  </details>
  </br>

📂보석으로 배낭 채우기

- 보석을 쪼갤 수 없음. 보석을 담거나 담지 않거나 두 가지 선택지 밖에 없음
  -> 0/1 knapsack (DP로 풀어야 함)
- 보석을 쪼갤 수 있음. -> Fractional knapsack

  ```
  무게 대비 가격이 높은 보석을 우선적으로 담기. 가격/무게 값이 큰 보석 부터 담기.
  가격/무게 값으로 내림차순 정렬 -> 배낭 크기 넘지 않는 선에서 순서대로 보석 담기

  * 가치/무게 내림차순 정렬
    jewels.sort(key=lambda x: -x[1]/x[0])
  ```

📂숫자 합치기

- 숫자를 합쳐 하나의 숫자로 만드는 데 필요한 최소 비용 출력하기
- 2개의 숫자를 골라 합치는 과정을 하나의 숫자만 남을 때까지 반복
- 숫자 a,b를 합치는데 드는 비용은 a+b </br>
  ex) `[1, 3, 8, 10]` : 1+3 / 4+8 / 12+10 -> 비용 : 4 + 12 + 22 </br>
  ex) `[50, 50, 50, 50]` : </br>

  - 왼쪽부터 차례대로 더할 경우) 50+50 / 100+50/ 150+50 -> 비용: 100 + 150 + 200 = 450
  - 50,50끼리 2쌍을 만들어 각각 더한 뒤 합할 경우) 50+50, 50+50/ 100+100 -> 비용: 100+ 100 + 200 = 400

  ```
  순서와 상관 없이 "가장 작은 2개의 숫자만" 선택하는 그리디로 풀 수 있음
  유사 알고리즘 : 허프만 코드

  ```

  <details>
  <summary>유형 문제</summary> </br>
  <div markdown="1">
    11399.py
  </div>
  </details>
  </br>
  </br>

# Graph

각 지점 : node(노드) 혹은 vertext(정점) 이라고 함
ex) sns라면 user, 지하철이라면 역 </br>
지점을 잇는 선 : edge(간선) ex) sns라면 팔로우 관계 </br>
간선의 가중치: 간선에 값이 있는 경우 그 값
정점A와 연결된 정점의 수 : degree(차수)

- 진입차수 (in-degree)
- 진출차수 (out-degree)

cycle 사이클이 있다 : 특정 지점에서 출발해서 다시 본래 지점으로 돌아올 수 있을 떄

### 인접행렬로 그래프 만들기

V = 정점의 수 </br>
E = 간선의 수 </br>
인접 행렬 : 1) V x V 크기의 2차원 배열 만들고 2) A -> B 로 가는 길이 있다면 값을 1, 없다면 0으로 지정 </br>
특정 정점 A, B가 연결되어 있는 지 확인 : O(1)</br>
특정 정점과 연결된 모든 정점 확인 : O(V)</br>
공간 복잡도 : O(V∗V)</br>

# DFS 깊이 우선 탐색

개념 : 루트 노드 혹은 하나의 노드에서 시작해서 다음 branch 분기로 넘어가기 전에 완벽히 탐색하고 넘어가는 법. 즉, 아래로 계속 내려가면서 탐색하다가 정점이 없으면 다음 분기로 넘어감. 깊게(deep)탐색

- 재귀 혹은 스택 으로 구현
- ✔ 방문 노드 검사 처리 필수 -> 검사하지 않으면 무한 루프에 빠질 수 있음
-

1. 인접 행렬 </br>

   1. i, j 노드가 연결되어 있다면 -> graph[i][j] = 1 </br>
      ex) 노드 1,2 연결 -> graph[1][2] = graph[2][1] = 1 </br>
      공간 복잡도 : O(V∗V)

   2. 재귀함수를 이용하여 탐색

   ```python
   # vertex : 정점
   # current_vertext : 정점과 연결된 노드 방문 시 현재 방문하는 노드
   def dfs(vertex):
    for current_vertext in range(1, VERTICES_NUM + 1):
        if graph[vertex][current_vertext] and not visited[current_vertext]:
            visited[current_vertext] = True
            dfs(current_vertext)

   ```

2. 인접 리스트 </br>
   V개의 동적 배열로 관리. i번쨰 노드와 연결된 모든 노드의 번호가 graph[i]에 들어가야 함. </br>
   공간복잡도 : O(V+E)</br>
   연결된 모든 정점이 graph[vertex] 안에 리스트 형태로 담기게 됨

   ```python
   # vertex : 정점
   # current_vertext : 정점과 연결된 노드 방문 시 현재 방문하는 노드
   def dfs(vertex):
    for current_vertext in graph[vertex]:
        if not visited[current_vertext]:
            visited[current_vertext] = True
            dfs(current_vertext)

   ```
   
## 대표문제

📂그리드 상에서 DFS탐색
2차원 격자에서 특정 시작점으로 부터 갈 수 있는 모든 지점 탐색.
- 현재 위치 (x,y)에서 갈 수 있는 곳 ( (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1) ) 이 있다면 방문 표시 해주고 다시 재귀함수 호출. -> dx dy 테크닉
- 갈 수 있는 지 없는 지 확인 하는 함수 필요 
  - (new_x, new_y)가 격자 안에 있어야 함
  - (new_x, new_y)에 방문한 적 없어야 함
  - (new_x, new_y)가 갈 수 있는 길이어야 함(폭탄 없어야 함)

### 재귀 사용 할 때 (필수)
```pyhon
import sys
sys.setrecursionlimit(10000)
```
### input 속도 문제 해결

```
import sys
input = sys.stdin.readline
```

### Min size

```python
import sys
INT_MIN = -sys.maxsize
```

### 실수표기

```python
print(f"{result:.4f}")
```

### 수열의 합

```python
1 + 1+2 + 1+2+3 + ...
for i in range(n):
    for j in range(i+1):
        print(i, j)

```

<details>
<summary>for루프</summary> </br>
<div markdown="1">
  ```python
  for i in range(n): 
    for j in range(i+1):
        print(i, j)
  0 0
  1 0
  1 1
  2 0
  2 1
  2 2
  3 0
  3 1
  3 2
  3 3
  4 0
  4 1
  4 2
  4 3
  4 4
```
</div>
</details>

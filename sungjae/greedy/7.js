/**
 * 프로그래머스 - 단속카메라(level3)
 * @param {number[]} routes
 * @returns
 */

// 교집합이 있다고 가정하고 생각해보면 최대한으로 다음 교집합까지 고려할수 있는 설치지점은 가장먼저 빠져나올 차량의 진출시점이다
// if 그전에 설치한다? => 이건 다음 교집합까지 생각하지 않은 사항임
// 그림으로 두 개의 교집합, 세 개의 교집합, 교집합이 없는 경우를 그려보자

// 사실 모든 차가 찍히게 설치하려면 각 차량의 진출시점 / 진입시점에 한대씩 달면 되지만,
// 어떻게하면 교집합을 고려할지 생각해보자

function solution(routes) {
  // 기본적으로 맨 처음 카메라를 설치하므로 1로 선언
  var answer = 1;
  // 진출시점을 기준으로 오름차순 정렬
  routes.sort((a, b) => a[1] - b[1]);
  // 맨 첫번째 카메라를 설치
  let camera = routes[0][1];
  // 이제 순회하면서, 다음 요소의 진입 시점이 할당된 값보다 작으면 진출시점의 값을 재할당하지 않음
  // 진입 시점이 할당된 값보다 크면 진출시점의 값을 재할당하고 카메라갯수를 ++
  for (let i = 1; i < routes.length; i++) {
    const curEnter = routes[i][0];
    const curExit = routes[i][1];
    if (camera >= curEnter) {
      continue;
    }
    camera = curExit;
    answer++;
  }
  return answer;
}

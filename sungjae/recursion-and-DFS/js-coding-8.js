/**
 * 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열 하는 방법을 모두 출력합니다.
 * @param {number} n
 * @param {number} m
 * @returns {number}
 */
function solution(n, m) {
  let answer = [];
  let temp = Array.from({ length: m }, () => 0);
  const DFS = (L) => {
    if (L === m) {
      answer.push([...temp]);
    } else {
      for (let i = 1; i <= n; i++) {
        temp[L] = i;
        DFS(L + 1);
      }
    }
  };
  DFS(0);
  return answer;
}

console.log(solution(3, 2));

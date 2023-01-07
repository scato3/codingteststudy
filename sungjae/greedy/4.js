/**
 * 큰 수의 법칙
 * @param {number} n
 * @param {number} m 총 횟수
 * @param {number} k 한 숫자당 최대로 더해지는
 * @param {number[]} arr
 */
function solution(n, m, k, arr) {
  let answer = 0;
  arr.sort((a, b) => b - a);
  const first = arr[0];
  const second = arr[1];
  let cnt = k;
  while (m > 0) {
    m--;
    if (cnt === 0) {
      answer += second;
      cnt += k;
    } else {
      answer += first;
      cnt--;
    }
  }
  return answer;
}

console.log(solution(5, 8, 3, [2, 4, 5, 4, 6]));
console.log(solution(5, 7, 2, [3, 4, 3, 4, 3]));

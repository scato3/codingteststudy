/**
 *
 * @param {number} n
 * @param {number[]} arr
 * @returns {number}
 */
function solution(n, arr) {
  let answer = Number.MIN_SAFE_INTEGER;
  const DFS = (L, sum) => {
    if (sum > n) return;
    if (L >= arr.length) {
      answer = Math.max(answer, sum);
    } else {
      DFS(L + 1, sum + arr[L]);
      DFS(L + 1, sum);
    }
  };
  DFS(0, 0);

  return answer;
}

console.log(solution(259, [81, 58, 42, 33, 61]));

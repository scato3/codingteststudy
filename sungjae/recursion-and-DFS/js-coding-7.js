/**
 * solve or not solve
 * @param {number} m 시간
 * @param {number[][]} arr [[점수, 시간] ,,, ]
 * @returns {number}
 */
function solution(m, arr) {
  let answer = 0;
  const DFS = (L, times, scores) => {
    if (times > m) return;
    if (L === arr.length) {
      answer = Math.max(answer, scores);
    } else {
      DFS(L + 1, times + arr[L][1], scores + arr[L][0]);
      DFS(L + 1, times, scores);
    }
  };
  DFS(0, 0, 0);
  return answer;
}

// prettier-ignore
console.log(solution(20, [[10, 5],[25, 12],[15, 8],[6, 3],[7, 4],]));

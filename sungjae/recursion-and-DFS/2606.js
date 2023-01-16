/**
 *
 * @param {number} n 컴퓨터의 수
 * @param {number[][]} arr 컴퓨터의 연결 현황
 */
function solution(n, arr) {
  const graph = [...new Array(n + 1)].map(() => []);
  const ch = Array.from({ length: n.length + 1 }, () => false);
  let answer = 0;

  for (const i of arr) {
    const [start, end] = i;
    graph[start].push(end);
    graph[end].push(start);
  }
  const DFS = (L) => {
    if (ch[L]) {
      console.log('already visit', L);
      return;
    } else {
      ch[L] = true;
      console.log('visit ', L);
      answer++;
      for (const dest of graph[L]) {
        DFS(dest);
      }
    }
  };
  DFS(1);
  return answer - 1;
}

const arr = [
  [1, 2],
  [2, 3],
  [1, 5],
  [5, 2],
  [5, 6],
  [4, 7],
];

console.log(solution(7, arr)); // 4

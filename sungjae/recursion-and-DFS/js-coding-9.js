function solution(arr, price) {
  let answer = Number.MAX_SAFE_INTEGER;
  const DFS = (L, sum) => {
    // 종료조건을 잘 생각하자
    if (sum > price) return;
    if (L >= answer) return;
    if (sum === price) {
      answer = Math.min(answer, L);
    } else {
      for (const coin of arr) {
        DFS(L + 1, sum + coin);
      }
    }
  };
  DFS(0, 0);
  return answer;
}

console.log(solution([1, 2, 5], 15));
console.log(solution([400, 500, 100], 800));

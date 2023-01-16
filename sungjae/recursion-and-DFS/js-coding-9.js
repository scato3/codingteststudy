function solution(arr, price) {
  let answer = Number.MAX_SAFE_INTEGER;
  const DFS = (L, sum) => {
    // 종료조건을 잘 생각하자

    // 이게없으면 무한정
    if (sum > price) return;
    // 이게있으면 효율성이 좋아짐
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

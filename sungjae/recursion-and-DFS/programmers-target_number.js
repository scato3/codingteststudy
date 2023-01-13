function solution(numbers, target) {
  var answer = 0;
  let temp = [];
  const DFS = (L, n) => {
    // 모든 경우를 다돌아야 한다
    // 만약 1번 테케의 경우 1 + 1 + 1을 했을때 3이라는 타겟이 되어서 종료가 되버릴수 있다
    if (L === numbers.length) {
      temp.push(n);
      // 그러면서도 그 계산결과가 타겟이어야 한다
      if (n === target) {
        answer++;
      }
    } else {
      // 더할수도 있고
      DFS(L + 1, n + numbers[L]);
      // 뺄 수도 있다
      DFS(L + 1, n - numbers[L]);
    }
  };
  DFS(0, 0);
  console.log(temp);
  return answer;
}

console.log(solution([1, 1, 1], 3)); // 1 => 2의 4제곱 - 1
// console.log(solution([1, 1, 1, 1, 1], 3)); // 5 => 2의 6제곱 - 1
// console.log(solution([4, 1, 2, 1], 4)); // 2 => 2의 5제곱 - 1

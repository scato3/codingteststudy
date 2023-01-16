function solution(m, numbers) {
  const ch = Array.from({ length: numbers.length }, () => false);
  const temp = Array.from({ length: m }, () => 0);
  let answer = [];
  const DFS = (L) => {
    if (L === m) {
      answer.push([...temp]);
    } else {
      for (let i = 0; i < numbers.length; i++) {
        if (ch[i] === false) {
          ch[i] = true;
          temp[L] = numbers[i];
          DFS(L + 1);
          ch[i] = false;
        }
      }
    }
  };
  DFS(0, numbers);
  return answer;
}

console.log(solution(2, [3, 6, 9]));

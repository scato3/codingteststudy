function solution(num) {
  let answer = 0;
  for (let i = 1; i <= num; i++) {
    const arr = (i + '').split('').map((x) => Number(x));
    const result = i + arr.reduce((acc, cur) => acc + cur, 0);
    if (result === num) {
      answer = i;
      break;
    }
  }
  return answer;
}

console.log(solution(216)); // 198

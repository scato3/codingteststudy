/**
 * 떡 먹는 호랑이
 * @param {number} day
 * @param {number} total
 */
function solution(day, total) {
  const answer = [];
  for (let i = 1; i <= 100000; i++) {
    for (let j = 1; j <= 100000; j++) {
      answer[0] = i;
      answer[1] = j;
      for (let k = 2; k < day; k++) {
        answer[k] = answer[k - 1] + answer[k - 2];
      }
      if (answer[day - 1] === total) {
        return [answer[0], answer[1]];
      }
    }
  }
}

console.log(solution(6, 41)); // 2 7
console.log(solution(7, 218)); // 10 21

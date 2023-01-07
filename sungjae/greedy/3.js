/**
 * 거스름돈
 * @param {number} money
 */
function solution(money) {
  const coins = [500, 100, 50, 10];
  let count = 0;
  for (const coin of coins) {
    count += Math.floor(money / coin);
    money = money % coin;
  }
  return count;
}

console.log(solution(1260));

// 숫자카드게임
function solution(arr) {
  const min = [];
  for (let i = 0; i < arr.length; i++) {
    min.push(Math.min(...arr[i]));
  }
  return Math.max(...min);
}

function solution2(arr) {
  const min = [];
  for (let i = 0; i < arr.length; i++) {
    let minVal = 10001;
    for (let j = 0; j < arr[0].length; j++) {
      if (arr[i][j] < minVal) minVal = arr[i][j];
    }
    min.push(minVal);
  }
  return Math.max(...min);
}

console.log(
  solution2([
    [3, 1, 2],
    [4, 1, 4],
    [2, 2, 2],
  ])
);
console.log(
  solution2([
    [7, 3, 1, 8],
    [3, 3, 3, 4],
  ])
);

function sol(arr) {
  const answer = [];
  for (let i = 0; i < arr.length; i++) {
    let temp = 1;
    for (let j = 0; j < arr.length; j++) {
      if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) {
        temp++;
      }
    }
    answer.push(temp);
  }
  return answer;
}

const test = [
  [55, 185],
  [58, 183],
  [88, 186],
  [60, 175],
  [46, 155],
];

console.log(sol(test)); // 2 2 1 2 5

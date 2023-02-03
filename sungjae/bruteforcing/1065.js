function solution(num) {
  if ((num + '').length < 3) {
    return num;
  }
  let cnt = 99;
  for (let j = 100; j <= num; j++) {
    let flag = true;
    const arr = (j + '').split('').map((x) => Number(x));
    const diff = arr[0] - arr[1];
    // console.log(j, diff);
    for (let i = 1; i < arr.length - 1; i++) {
      const prev = arr[i];
      const next = arr[i + 1];
      if (prev - next !== diff) {
        flag = false;
      }
    }
    if (flag) {
      // console.log(j);
      cnt++;
    }
  }
  return cnt;
}

// console.log(solution(123)); //
console.log(solution(110)); //99
console.log(solution(1)); //1
console.log(solution(210)); //105
console.log(solution(1000)); //144
console.log(solution(500)); //119

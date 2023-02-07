0666;
1666;
2666;
3666;
4666;
5666;
6661;
6662;
6663;
6664;
6665;
6666;
6667;
6668;
6669;
7666;
8666;
9666;

10666;
11666;
12666;
13666;
14666;
15666;
16661;
16662;
16663;
16664;
16665;
16666;
16667;
16668;
16669;
17666;
18666;
19666;

20666;

function solution(n) {
  const arr = [666];
  let startNum = 667;
  while (arr.length < n) {
    startNum++;
    if ((startNum + '').includes('666')) {
      arr.push(startNum);
    }
  }
  return arr[arr.length - 1];
}

console.log(solution(2));
console.log(solution(3));
console.log(solution(6));
console.log(solution(187));
console.log(solution(500));

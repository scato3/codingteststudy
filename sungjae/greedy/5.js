// 회의실배정-백준
function solution(arr) {
  const stack = [];
  arr.sort((a, b) => (a[1] - b[1] === 0 ? a[0] - b[0] : a[1] - b[1]));
  let prevEnd = 0;
  arr.forEach(([start, end]) => {
    if (start < prevEnd) {
      return;
    }
    prevEnd = end;
    stack.push([start, end]);
  });
  return stack.length;
}

console.log(
  solution([
    [1, 4],
    [3, 5],
    [0, 6],
    [5, 7],
    [3, 8],
    [5, 9],
    [6, 10],
    [8, 11],
    [8, 12],
    [2, 13],
    [12, 14],
  ])
);

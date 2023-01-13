function solution(arr) {
  let answer = 0;
  const ch = Array.from({ length: arr.length }, () => Array.from({ length: arr[0].length }, () => false));
  const DFS = (x, y) => {
    // 범위를 넘거나 방문하였다면 리턴시킨다
    if (x < 0 || y < 0 || x >= arr.length || y >= arr[0].length || ch[x][y]) {
      return;
    }
    if (arr[x][y] === 0) {
      ch[x][y] = true;
      DFS(x - 1, y); // up
      DFS(x + 1, y); // down
      DFS(x, y - 1); // left
      DFS(x, y + 1); // right
      // 처음 방문하는 것만 체크를 한다...?
      // 17라인을 생각해내지못함
      return true;
    }
  };
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[0].length; j++) {
      if (DFS(i, j)) {
        console.log(i, ',', j, '방문합니다');
        answer++;
      }
    }
  }
  console.log(ch);
  return answer;
}

// prettier-ignore
console.log(solution([[0, 0, 1, 1, 0],[0, 0, 0, 1, 1],[1, 1, 1, 1, 1],[0, 0, 0, 0, 0]]));

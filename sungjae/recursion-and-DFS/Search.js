function solution(arr) {
  const stack = [];
  const ch = Array.from({ length: arr.length + 1 }, () => false);
  const DFS = (L) => {
    console.log('DFS(', L, ') 을 호출했습니다.');
    if (ch[L]) {
      console.log('이미', L, '을 방문하여 리턴합니다.');
      return;
    } else {
      ch[L] = true;
      stack.push(L);
      console.log(L, '<= 을 방문했습니다');
      for (const node of arr[L]) {
        DFS(node);
      }
    }
  };
  DFS(1);
  return stack;
}
//                            1        2          3       4       5      6       7         8
console.log(solution([[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]));

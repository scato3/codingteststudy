function solution(num) {
  const DFS = (v) => {
    if (v > 7) {
      console.log("what's return? : ", v);
      return;
    } else {
      // console.log('전위순회 : ', v);
      DFS(2 * v);
      // console.log('중위순회 : ', v);
      DFS(2 * v + 1);
      console.log('후위순회 : ', v);
    }
  };
  DFS(num);
}

solution(1);

// 전위 => 부모 왼쪽 오른쪽
// 중위 => 왼쪽 부모 오른쪽
// 전위 => 왼쪽 오른쪽 부모

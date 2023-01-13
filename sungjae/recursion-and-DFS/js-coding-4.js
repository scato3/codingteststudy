// 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램 을 작성하세요.

function solution(num) {
  // 0 == not include
  let ch = Array.from({ length: num + 1 }, () => 0);
  const DFS = (n) => {
    if (n > num) {
      let temp = [];
      for (let i = 1; i <= ch.length; i++) {
        if (ch[i] === 1) {
          temp.push(i);
        }
      }
      if (temp.length === 0) {
        return;
      }
      console.log(temp);
    } else {
      ch[n] = 1;
      DFS(n + 1);
      ch[n] = 0;
      DFS(n + 1);
    }
  };
  DFS(1);
}

solution(3);

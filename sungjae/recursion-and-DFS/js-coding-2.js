// 10진수 num이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용 해서 출력해야 합니다.

// idea

// 2의 n제곱수 최대로 쪼갠다 => 계속...

function solution(num) {
  let answer = '';
  const dfs = (n) => {
    if (n === 0) return;
    console.log('start : ', n);
    dfs(Math.floor(n / 2));
    answer += n % 2;
    console.log('end : ', n);
  };
  dfs(num);
  return answer;
}

console.log(solution(11));

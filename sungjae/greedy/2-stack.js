/**
 *
 * @param {string} number
 * @param {number} k
 */
function solution(number, k) {
  let answer = '';
  // 몇 개 뺐는지 카운트해서, k가 되는순간 로직을 중지합니다
  let cnt_delete = 0;
  // stack에 큰 수만 담을겁니다 - k번 뺄때까지
  let stack = [];

  for (let i = 0; i < number.length; i++) {
    while (stack.length !== 0) {
      // 카운트가 끝났으면 루프를 빠져나온다.
      if (cnt_delete === k) break;

      // 현재 스택에 있는 마지막 값이 비교하는 숫자보다 작다면 제거하고 카운트를 1 증가한다.
      if (stack[stack.length - 1] < number[i]) {
        ++cnt_delete;
        stack.pop();
      } else {
        break;
      }
    }

    // 스택이 비어있다면 다음 숫자를 넣는다.
    stack.push(number[i]);
  }

  // answer = stack.join('').substring(0, number.length - k);
  answer = stack.join('');
  return answer;
}

console.log(solution('1924', 2)); //94
console.log(solution('1231234', 3)); //3234
console.log(solution('4177252841', 4)); //775841

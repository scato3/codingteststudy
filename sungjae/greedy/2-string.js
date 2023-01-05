function solution(number, k) {
  let temp = [];
  while (temp.length < k) {
    for (let i = 0; i < number.length - 1; i++) {
      const first = number[i];
      const second = number[i + 1];
      if (first < second) {
        number = number.substring(0, i) + number.substring(i + 1, number.length);
        temp.push(first);
        break;
      }
    }
  }
  return number;
}

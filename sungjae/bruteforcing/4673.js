function solution() {
  const tempFunc = (num) => {
    let result = num;
    const str = num.toString();
    for (let i = 0; i < str.length; i++) {
      result += Number(str[i]);
    }
    return result;
  };
  // 기능 체크 완료
  // console.log(tempFunc(33)); // 33 3 3 = 39
  // console.log(tempFunc(11)); // 11 1 1 = 13
  // console.log(tempFunc(39)); // 39 3 9 = 51

  const arr = [];
  for (let i = 1; i <= 10000; i++) {
    const el = tempFunc(i);
    arr.push(el);
  }

  const set = new Set();
  for (let i = 1; i <= 10000; i++) {
    const el = tempFunc(i);
    set.add(el);
  }

  // 약 천여개의 차이가 있음 => 그렇다면 탐색시 조금더(아주약간) 효율이 좋다
  // console.log(arr.length);
  // console.log(set.size);

  for (let i = 1; i <= 10000; i++) {
    if (!set.has(i)) {
      console.log(i);
    }
  }
}

solution();

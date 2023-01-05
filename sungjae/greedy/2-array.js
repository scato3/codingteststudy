/**
 *
 * @param {string} number
 * @param {number} k
 */
function solution(number, k) {
  const target_num = number.length - k;
  const arr = number.split('');
  while (arr.length > target_num) {
    for (let i = 0; i < arr.length - 1; i++) {
      const prev = arr[i];
      const next = arr[i + 1];
      if (prev < next) {
        arr.splice(i, 1);
        break;
      }
    }
  }
  return arr.join('');
}

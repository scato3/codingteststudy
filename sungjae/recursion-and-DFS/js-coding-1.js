function printN(num) {
  if (num === 0) return;
  printN(num - 1);
  console.log(num);
}

printN(5);

function solution(k, dungeons) {
  const ch = Array.from({ length: dungeons.length }).fill(false);

  // 탐색레벨
  let Level = 0;

  const DFS = (L, k) => {
    Level = Math.max(L, Level);
    if (Level === dungeons.length) {
      return;
    }
    for (let i = 0; i < dungeons.length; i++) {
      const [min, consume] = dungeons[i];
      if (k >= min && !ch[i]) {
        ch[i] = true;
        DFS(L + 1, k - consume);
        ch[i] = false;
      }
    }
  };
  DFS(0, k);
  return clearCnt;
}

// prettier-ignore
console.log(solution(80, [[80, 20], [50, 40], [30, 10]])); // 3

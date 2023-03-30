# 백준 1339 단어 수학 GOLD lV
# https://www.acmicpc.net/problem/1339

n = int(input())
alpha = [0 for i in range(26)]

for _ in range(n):
    word = input()

    for i in range(len(word)):
        alpha[ord(word[i]) - ord('A')] += 10 ** (len(word) - 1 - i)

alpha.sort(reverse=True)
num = 9
ans = 0

for i in alpha:
    if i == 0 or num == 0:
        break
    ans += i * num
    num -= 1

print(ans)

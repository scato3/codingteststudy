# 백준 1213 팰린드롬 만들기 SILVER lll
# https://www.acmicpc.net/problem/1213

alpha =[0 for _ in range(26)]
k = input()

for i in k:
    alpha[ord(i) - 65] += 1

cnt = 0
odd_alpha = ''
pha = ''
for i in range(26):
    if alpha[i] % 2 == 1:
        cnt += 1
        odd_alpha += chr(i+65)
    pha += chr(i+65) * (alpha[i] // 2)

if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(pha + odd_alpha + pha[::-1])





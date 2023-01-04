# 5885
# 거스름돈
"""
잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고,
거스름돈 개수가 가장 적게 잔돈을 준다.

1000엔 지폐를 한장 냈을 때,
잔돈의 개수를 구해라.

예제 입력
380 //620 500 100 10 10
출력
4

"""
# 오답
price = int(input())
change = 1000-price
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in coins:
    if change - i > 0:
        cnt += (change // i)
        change %= i
        # change -= (i * (change//i)) -> 오답

print(cnt)

# 통과
price = int(input())
change = 1000-price
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in coins:
    cnt += (change // i)
    change %= i
print(cnt)

# 통과
change = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
count = 0
for i in coins:
    count += change // i
    change %= i
print(count)

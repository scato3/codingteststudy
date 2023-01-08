# 백준 2864 5와 6의 차이 BRONZE ll
# https://www.acmicpc.net/problem/2864

a, b = input().split()
min_sum = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max_sum = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min_sum, max_sum)
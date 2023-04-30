n, g = input().split()
player = [input() for _ in range(int(n))]
player = list(set(player))

if g == 'Y':
    print(len(player))
elif g == 'F':
    print(len(player) // 2)
else:
    print(len(player) // 3)
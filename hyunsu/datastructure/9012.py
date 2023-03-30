n = int(input())

for _ in range(n):
    k = input()
    stack = []

    for i in k:
        if i == '(':
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            print('NO')
            break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')



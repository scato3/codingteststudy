import sys
input=sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    com = input().split()

    if len(com) == 1:
        if com[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()

    else:
        func, x = com[0], com[1]
        x = int(x)
        if func == 'add':
            s.add(x)
        elif func == 'remove':
            s.discard(x)
        elif func == 'check':
            print(1 if x in s else 0)
        elif func == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)

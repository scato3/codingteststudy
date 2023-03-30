import sys
from collections import deque
n = int(sys.stdin.readline())
stack = deque()

for _ in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push_front':
        stack.appendleft(com[1])
    elif com[0] == 'push_back':
        stack.append(com[1])
    elif com[0] == 'pop_front':
        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif com[0] == 'pop_back':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if stack:
            print(stack[-1])
        else:
            print(-1)
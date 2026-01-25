stack = []

N = int(input())

for _ in range(N):
    cmd = input()

    if len(cmd) >= 6 and cmd.startswith('push'):
        stack.append(int(cmd[5:]))
    elif cmd == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
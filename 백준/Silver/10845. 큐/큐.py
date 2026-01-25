from collections import deque
q = deque()

N = int(input())

for _ in range(N):
    cmd = input()

    if len(cmd) >= 6 and cmd.startswith('push'):
        q.append(int(cmd[5:]))
    elif cmd == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    else: # cmd == 'back'
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
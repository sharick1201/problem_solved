from collections import deque

d = deque()

T = int(input())

for _ in range(T):
    txt = input()

    if txt.startswith('push_front'):
        d.appendleft(txt[11:])

    elif txt.startswith('push_back'):
        d.append(txt[10:])

    elif txt == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
            
    elif txt == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())

    elif txt == 'size':
        print(len(d))

    elif txt == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)

    elif txt == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
            
    elif txt == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
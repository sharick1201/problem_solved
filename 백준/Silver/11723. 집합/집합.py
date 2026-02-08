import sys

# 입력 엄청 받아야하니까 readline으로

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    cmd = sys.stdin.readline().strip().split()
    op = cmd[0]

    if op == 'add':
        S.add(int(cmd[1]))
    elif op == 'remove':
        S.discard(int(cmd[1]))  # discard는 없으면 무시 / remove는 없으면 에러
    elif op == 'check':
        print(1 if int(cmd[1]) in S else 0)
    elif op == 'toggle':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            S.add(int(cmd[1]))
    elif op == 'all':
        # S = new_S # 파이썬 set은 얕은복사가 된다고 함
        S = set(range(1, 21))
    elif op == 'empty':
        S.clear()
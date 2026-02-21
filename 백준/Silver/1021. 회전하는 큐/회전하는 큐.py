from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, N + 1))
ans = 0

for target in targets:
    target_idx = dq.index(target)
    
    # 큐 앞쪽에 있으면 왼쪽으로 이동
    # 아니면 오른쪽으로 이동할래
    if target_idx <= len(dq) // 2:
        ans += target_idx
        dq.rotate(-target_idx)
    else:
        ans += len(dq) - target_idx
        dq.rotate(len(dq) - target_idx)
    
    dq.popleft()
    
print(ans)
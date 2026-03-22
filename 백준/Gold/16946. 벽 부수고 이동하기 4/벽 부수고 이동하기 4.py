"""
벽에 대해 DFS 하면 시간초과날듯
벽 아닌 공간에 대해서 DFS -> 16724 피리부는사나이 처럼 스택 써서
DFS로 하려는 것: 벽이 아닌 공간 컴포넌트 갯수 저장
"""
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(sy, sx):
    visited[sy][sx] = 1
    trails = set()  # walls
    stk = [(sy, sx)]
    now_ans = 1

    while stk:
        y, x = stk.pop()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            # 범위밖, 방문, 벽
            if not (0 <= ny < N and 0 <= nx < M): continue
            if arr[ny][nx] == 1:
                trails.add((ny, nx))
                continue
            if visited[ny][nx]: continue
            now_ans += 1
            visited[ny][nx] = 1
            stk.append((ny, nx))


    # visited 에 컴포넌트 크기 저장
    for ty, tx in list(trails):
        visited[ty][tx] += now_ans


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            dfs(i, j)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            print((visited[i][j] + 1) % 10, end="")
        else:
            print(0, end="")
    print()
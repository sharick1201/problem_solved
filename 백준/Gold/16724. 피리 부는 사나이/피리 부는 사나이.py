"""
싸이클의 갯수를 찾으면 됨
"""

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
dydx_mapping = {"U": 0, "D": 1, "L": 2, "R": 3}

# 재귀로 하면 RecursionError 날듯 -> 스택으로
def dfs(sy, sx, seed):
    global ans

    stk = [(sy, sx)]

    while stk:
        y, x = stk.pop()

        # 종료조건
        # 내가 나의 사이클을 만들었으면
        if visited[y][x] == seed:
            ans += 1
            return
        # 다른 사이클에 합류되면
        elif 0 < visited[y][x]:
            return

        # 단위작업
        visited[y][x] = seed

        ny = y + dy[dydx_mapping[arr[y][x]]]
        nx = x + dx[dydx_mapping[arr[y][x]]]

        stk.append((ny, nx))


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
seed = 1
ans = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i, j, seed)
            seed += 1

print(ans)
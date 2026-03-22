"""
25'000'000

연구소는 크기가 N * N
빈 칸, 벽, 활성바이러스, 비활성바이러스

모든 바이러스는 비활성이고, 활성상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제 -> 1초가 걸림
승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.

0은 빈 칸
1은 벽
2는 바이러스의 위치

BFS

연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간

1. 비활성 바이러스의 좌표들을 모은다.
2. 조합을 구함
3. 그 조합을 큐에 넣고 BFS
    빈칸이면 방문에 +1
    시간 갱신
    비활성 바이러스면 방문에 +1
    시간 갱신 안 함

    그 조합이 모든 빈 칸을 무사히 방문했는지 확인한다.
"""
from collections import deque
from itertools import combinations

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(start_lst):
    visited = [[-1] * N for _ in range(N)]
    q = deque(start_lst)
    cost = 0

    for sy, sx in start_lst:
        visited[sy][sx] = 0

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if not (0 <= ny < N and 0 <= nx < N): continue
            if visited[ny][nx] != -1: continue
            if arr[ny][nx] == 1: continue

            if arr[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                cost = max(cost, visited[ny][nx])

            if arr[ny][nx] == 2:
                visited[ny][nx] = visited[y][x] + 1

            q.append((ny, nx))

    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and arr[i][j] == 0:
                return 10 ** 8

    return cost



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_lst.append((i, j))

ans = 10 ** 8
for comb in combinations(virus_lst, M):
    ans = min(ans, bfs(list(comb)))

print(ans if ans != 10 ** 8 else -1)
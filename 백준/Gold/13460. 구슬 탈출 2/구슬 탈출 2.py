from collections import deque

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)


def move(y, x, dy, dx):
    count = 0
    # 다음 칸이 벽이 아니고, 현재 칸이 구멍이 아닐 때까지 이동
    while arr[y + dy][x + dx] != '#' and arr[y][x] != 'O':
        y += dy
        x += dx
        count += 1
    return y, x, count


def bfs(rsy, rsx, bsy, bsx):
    q = deque([(0, rsy, rsx, bsy, bsx)])
    visited = set([(rsy, rsx, bsy, bsx)])

    while q:
        time, ry, rx, by, bx = q.popleft()

        if time >= 10:
            break

        for dy, dx in [UP, DOWN, LEFT, RIGHT]:
            # 빨간 구슬 이동
            nry, nrx, r_cnt = move(ry, rx, dy, dx)
            # 파란 구슬 이동
            nby, nbx, b_cnt = move(by, bx, dy, dx)

            # 파란 구슬이 구멍에 빠지면 무조건 실패 (다음 방향 탐색)
            if arr[nby][nbx] == 'O':
                continue

            # 빨간 구슬이 구멍에 빠지면 성공!
            if arr[nry][nrx] == 'O':
                return time + 1

            # 두 구슬이 같은 위치에 도달했을 경우 (벽에 부딪힌 상황)
            if nry == nby and nrx == nbx:
                # 더 많이 이동한 구슬이 뒤에 있었던 구슬임 -> 한 칸 뒤로 뺌
                if r_cnt > b_cnt:
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx

            # 방문하지 않은 상태라면 큐에 삽입
            if (nry, nrx, nby, nbx) not in visited:
                visited.add((nry, nrx, nby, nbx))
                q.append((time + 1, nry, nrx, nby, nbx))

    return -1


# 입력 처리
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

sred_y, sred_x, sblue_y, sblue_x = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            sred_y, sred_x = i, j
            arr[i][j] == '.'

        elif arr[i][j] == 'B':
            sblue_y, sblue_x = i, j
            arr[i][j] == '.'

print(bfs(sred_y, sred_x, sblue_y, sblue_x))

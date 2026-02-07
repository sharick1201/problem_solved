dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def backtracking(y, x, apple_cnt, distance):
    global ans

    # 가지치기 추가
    if distance > ans:
        return

    if apple_cnt == 3:
        ans = min(ans, distance)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not (0 <= ny < 5 and 0 <= nx < 5):
            continue

        # 장애물이 있어서 거기로 못 지나가면
        if board[ny][nx] == -1:
            continue

        # 다음으로 갈 수 있으면
        if board[ny][nx] == 1:
            apple_cnt += 1

        temp = board[y][x]
        board[y][x] = -1

        backtracking(ny, nx, apple_cnt, distance + 1)

        if board[ny][nx] == 1:
            apple_cnt -= 1

        board[y][x] = temp


board = [list(map(int, input().split())) for _ in range(5)]    # 5x5
start_y, start_x = map(int, input().split())

ans = 25 + 1
backtracking(start_y, start_x, 0, 0)

if ans == 25 + 1:
    print(-1)
else:
    print(ans)

    # 오 왼 위 아래
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


# 각 온풍기의 바람 할당(4부터 1까지)
# 인자 온풍기방향, 지금할당해야하는수, 직전에할당된좌표들
def blow_winds(rdir, added_temp, prev_yx_lst):
    # 종료조건
    if added_temp == 0:
        return

    now_yx = set()
    
    # 단위작업
    for y, x in prev_yx_lst:
        for d in [-1, 0, 1]:
            ny = y + (d if dy[rdir] == 0 else dy[rdir])
            nx = x + (d if dx[rdir] == 0 else dx[rdir])

            # 범위밖이면
            if not (0 <= ny < N and 0 <= nx < M):
                continue

            # 만약 이미 있다면
            if (ny, nx) in now_yx:
                continue

            # 아니면 벽 때문에 못 간다면
            if d == -1:
                # 내 위:
                ddy = -1 if rdir <= 1 else 0
                ddx = 0 if rdir <= 1 else -1

                up_yx = (y + ddy, x + ddx)
                # 내 위에 있는지
                if ((y, x), up_yx) in walls or (up_yx, (y, x)) in walls:
                    continue

                # 도착점 직전에 있는지
                if (up_yx, (ny, nx)) in walls or ((ny, nx), up_yx) in walls:
                    continue

            elif d == 0:
                if ((y, x), (ny, nx)) in walls or ((ny, nx), (y, x)) in walls:
                    continue

            else:
                # 내 아래:
                ddy = 1 if rdir <= 1 else 0
                ddx = 0 if rdir <= 1 else 1

                down_yx = (y + ddy, x + ddx)
                # 내 아래에 있는지
                if ((y, x), down_yx) in walls or (down_yx, (y, x)) in walls:
                    continue
                # 도착점 직전에 있는지
                if (down_yx, (ny, nx)) in walls or ((ny, nx), down_yx) in walls:
                    continue

            # 다 아니면 추가하고 격자에 바람 추가
            now_yx.add((ny, nx))
            temperature_arr[ny][nx] += added_temp

    blow_winds(rdir, added_temp - 1, list(now_yx))




def change_temperature():
    # 그 좌표의 상하좌우 체크했는지 확인한다.
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    for cy in range(N):
        for cx in range(M):
            for d in range(4):
                ny = cy + dy[d]
                nx = cx + dx[d]

                # 범위밖
                if not (0 <= ny < N and 0 <= nx < M):
                    continue

                # 이미 방문한 방향이라면
                if visited[cy][cx][d]:
                    continue

                # 벽이 있다면
                if ((cy, cx), (ny, nx)) in walls or ((ny, nx), (cy, cx)) in walls:
                    continue

                # 이제 (cy, cx) - (ny, nx) 간 온도 조절
                # 온도 상대적으로 더 큰게 누군지 확인하고 추가
                # 내가 더 크다면
                if temperature_arr[cy][cx] > temperature_arr[ny][nx]:
                    val = abs(temperature_arr[ny][nx] - temperature_arr[cy][cx]) // 4
                    new_temp_arr[cy][cx] -= val
                    new_temp_arr[ny][nx] += val
                # 내가 더 작다면
                elif temperature_arr[cy][cx] < temperature_arr[ny][nx]:
                    val = abs(temperature_arr[ny][nx] - temperature_arr[cy][cx]) // 4
                    new_temp_arr[cy][cx] += val
                    new_temp_arr[ny][nx] -= val

                # 방문처리
                visited[cy][cx][d] = True
                visited[ny][nx][d ^ 1] = True


# 바깥쪽 온도 1씩 감소
def decrease_outer_temperature():
    for x in range(M):
        if temperature_arr[0][x] > 0:
            temperature_arr[0][x] -= 1
        if temperature_arr[N-1][x] > 0:
            temperature_arr[N-1][x] -= 1

    for y in range(1, N-1):
        if temperature_arr[y][0] > 0:
            temperature_arr[y][0] -= 1
        if temperature_arr[y][M-1] > 0:
            temperature_arr[y][M-1] -= 1



N, M, K = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(N)]

temperature_arr = [[0] * M for _ in range(N)]     # 그 y,x 의 온도
radiator_lst = []    # 온풍기 정보의 리스트          (y, x, dir)
checkpoint_lst = []  # 체크해야 하는 칸들의 리스트    (y, x)
walls = set()     # 벽과 인접한 칸 두개 ((), ())


# 0. 준비작업: 입력받은 판들 정보에 맞게 자료구조에 넣는다.
for i in range(N):
    for j in range(M):
        # 온도 조사해야 하는 칸
        if input_arr[i][j] == 5:
            checkpoint_lst.append((i, j))
        # 온풍기
        elif input_arr[i][j] != 0:
            radiator_lst.append((i, j, input_arr[i][j] - 1))


# 벽 넣기
W = int(input())
for _ in range(W):
    y, x, t = map(int, input().split())

    # 0-indexed 로 변환
    y -= 1
    x -= 1

    if t == 0:
        walls.add(((y, x), (y - 1, x)))
    else:
        walls.add(((y, x), (y, x + 1)))


for choko in range(1, 101):
    # 1. 온풍기 바람
    for ry, rx, rdir in radiator_lst:
        ny = ry + dy[rdir]
        nx = rx + dx[rdir]
        # 범위 내+벽 없으면 일단 5 박고 시작. 아니면 시작도 못함
        if not (0 <= ny < N and 0 <= nx < M):
            continue
        if ((ry, rx), (ny, nx)) in walls or ((ny, nx), (ry, rx)) in walls:
            continue
        temperature_arr[ny][nx] += 5
        blow_winds(rdir, 4, [(ny, nx)])

    # 2. 온도조절
    new_temp_arr = [row[:] for row in temperature_arr]
    change_temperature()
    temperature_arr = [row[:] for row in new_temp_arr]

    # 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    decrease_outer_temperature()

    # 4. 온도를 조사해야 하는 칸들의 온도가 K 이상인지 확인
    for y, x in checkpoint_lst:
        if temperature_arr[y][x] < K:
            break
    else:
        print(choko)
        break

else:
    print(101)

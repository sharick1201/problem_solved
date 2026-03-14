from collections import deque

# 리팩토링 2
# 주사위 회전 로직 변경 2: (선)헌석님 방식(덱 2개를 활용해 깔끔하게 rotate) => 하드코딩할 게 없어짐

# 헐 완전깔끔... It works... and it's pretty
def roll_dice(dice_dir):
    global dice_horizontal, dice_vertical
    # 오른쪽으로
    if dice_dir == 0:
        dice_horizontal.rotate(1)
        dice_vertical[0], dice_vertical[2] = dice_horizontal[0], dice_horizontal[2]

    # 아래로
    elif dice_dir == 1:
        dice_vertical.rotate(1)
        dice_horizontal[0], dice_horizontal[2] = dice_vertical[0], dice_vertical[2]

    # 왼쪽으로
    elif dice_dir == 2:
        dice_horizontal.rotate(-1)
        dice_vertical[0], dice_vertical[2] = dice_horizontal[0], dice_horizontal[2]

    # 위로
    elif dice_dir == 3:
        dice_vertical.rotate(-1)
        dice_horizontal[0], dice_horizontal[2] = dice_vertical[0], dice_vertical[2]



# 값이 arr[dice_y][dice_x]랑 같은 칸의 갯수를 세는 함수
# return 없음
def cnt_by_dfs(y, x):
    global same_val_cnt, target_val
    # 단위작업
    # arr[dice_y][dice_x]랑 같은 것들만 여기 도달
    same_val_cnt += 1
    visited[y][x] = True

    # 다음으로...
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        # 범위내
        if not (0 <= ny < N and 0 <= nx < M): continue
        # 미방문
        if visited[ny][nx]: continue
        # 조건에 맞아야
        if arr[ny][nx] != target_val: continue

        # target_val이면 ㄱㄱ
        cnt_by_dfs(ny, nx)



""" 입력받기 """
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # N x M

""" 필요한 자료구조 생성 """
    # 시계방향
    # 우 하 좌 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# # 2
# 4 1 3
# # 5
# # 6
dice_horizontal = deque([1, 3, 6, 4])
dice_vertical = deque([1, 5, 6, 2])
dir_idx = 0
dice_y, dice_x = 0, 0

ans = 0

for _ in range(K):
    """ 1. 주사위 이동 """
    ny = dice_y + dy[dir_idx]
    nx = dice_x + dx[dir_idx]

    # 범위 밖이면 이동방향 바꾸고 ny, nx도 갱신
    if not (0 <= ny < N and 0 <= nx < M):
        # 얘는 항상 범위내에 있는 게 보장됨. 인덱스 에러가 나면 여기서 잘못했을 가능성이 있다.
        dir_idx = (dir_idx + 2) % 4
        ny = dice_y + dy[dir_idx]
        nx = dice_x + dx[dir_idx]

    dice_y = ny
    dice_x = nx

    # roll the dice~~
    roll_dice(dir_idx)

    """ 2. 점수 계산 """
    visited = [[False] * M for _ in range(N)]
    target_val = arr[dice_y][dice_x]
    same_val_cnt = 0
    cnt_by_dfs(dice_y, dice_x)

    ans += same_val_cnt * target_val

    """ 3. 주사위의 다음 이동 방향 결정 """
    if dice_horizontal[2] > arr[dice_y][dice_x]:
        dir_idx = (dir_idx + 1) % 4
    elif dice_horizontal[2] < arr[dice_y][dice_x]:
        dir_idx = (dir_idx - 1) % 4

print(ans)


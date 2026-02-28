"""
출력: 각 이동에서 획득하는 점수의 "합"


1. 다음 이동 방향에 칸이 있다면 -> ny, nx로 간다.
   다음 이동 방향에 칸이 없다면 -> 이동 방향 "반대"로 한 다음 그 반대칸으로 간다.

    - 주사위 바닥이 있는 곳 dice_y, dice_x 갱신
    - 주사위 위치에 맞게 회전

2. 주사위가 도착한 칸(arr[ny][nx]) 에 대한 점수 획득
    - 점수란? 값이 arr[ny][nx] 인 칸 dfs해서 방문한 칸 갯수 * arr[ny][nx]


3. 주사위의 다음 이동 방향 결정
    주사위의 아랫면에 있는 정수 A(주사위 눈) 와 주사위가 있는 칸 (x, y)에 있는 정수를 비교
        A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
        A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
        A = B인 경우 이동 방향에 변화는 없다.


주사위를 회전시키는 게 아님. 이동 방향을 회전시키는 것
방문한 칸의 점수가 사라지지는 않음
"""

# 주사위 회전에 따라 달라지는 눈-위치를 다시 매핑
# return 없음
def roll_dice(dice_dir):
    global dice
    new_dice = [0] * 6
    # 오른쪽으로
    if dice_dir == 0:
        new_dice[0] = dice[5]  # 바닥  3
        new_dice[1] = dice[1]  # 상   2
        new_dice[2] = dice[4]  # 천장  4
        new_dice[3] = dice[3]  # 하    5
        new_dice[4] = dice[0]  # 왼쪽  6
        new_dice[5] = dice[2]  # 오른쪽 1

    # 아래로
    elif dice_dir == 1:
        new_dice[0] = dice[3]  # 바닥  5
        new_dice[1] = dice[0]  # 상    6
        new_dice[2] = dice[1]  # 천장  2
        new_dice[3] = dice[2]  # 하    1
        new_dice[4] = dice[4]  # 왼쪽  4
        new_dice[5] = dice[5]  # 오른쪽 3

    # 왼쪽으로
    elif dice_dir == 2:
        new_dice[0] = dice[4]  # 바닥  4
        new_dice[1] = dice[1]  # 상    2
        new_dice[2] = dice[5]  # 천장  3
        new_dice[3] = dice[3]  # 하    5
        new_dice[4] = dice[2]  # 왼쪽  1
        new_dice[5] = dice[0]  # 오른쪽 6

    # 위로
    elif dice_dir == 3:
        new_dice[0] = dice[1]  # 바닥  2
        new_dice[1] = dice[2]  # 상    1
        new_dice[2] = dice[3]  # 천장  5
        new_dice[3] = dice[0]  # 하    6
        new_dice[4] = dice[4]  # 왼쪽  4
        new_dice[5] = dice[5]  # 오른쪽 3

    dice = new_dice


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

    # idx: 위치 / val: 주사위 눈
    # 바닥,상,천장,하,좌,우(우=동쪽)
dice = [6, 2, 1, 5, 4, 3]
dir_idx = 0
dice_y, dice_x = 0, 0

ans = []  # 디버깅 하기 쉽게 리스트로 관리했음

for _ in range(K):
    """ 1. 주사위 이동 """
    # 1. 다음 이동 방향에 칸이 있다면 -> ny, nx로 간다.
    #    다음 이동 방향에 칸이 없다면 -> 이동 방향 "반대"로 한 다음! 그 반대칸으로 간다.
    #     - 주사위 바닥이 있는 곳 dice_y, dice_x 갱신
    #     - 주사위 위치에 맞게 회전
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
    # 2. 주사위가 도착한 칸(arr[ny][nx]) 에 대한 점수 획득
    #     - 점수란? 값이 arr[ny][nx] 인 칸 dfs해서 방문한 칸 갯수 * arr[ny][nx]
    visited = [[False] * M for _ in range(N)]
    target_val = arr[dice_y][dice_x]
    same_val_cnt = 0
    cnt_by_dfs(dice_y, dice_x)

    ans.append(same_val_cnt * target_val)

    """ 3. 주사위의 다음 이동 방향 결정 """
    # 3. 주사위의 아랫면에 있는 정수 A(주사위 눈) 와 주사위가 있는 칸 (x, y)에 있는 정수를 비교
    #         A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    #         A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    #         A = B인 경우 이동 방향에 변화는 없다.
    if dice[0] > arr[dice_y][dice_x]:
        dir_idx = (dir_idx + 1) % 4
    elif dice[0] < arr[dice_y][dice_x]:
        dir_idx = (dir_idx - 1) % 4

print(sum(ans))


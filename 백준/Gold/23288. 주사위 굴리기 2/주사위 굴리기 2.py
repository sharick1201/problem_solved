# 리팩토링 1
# 주사위 회전 로직 변경 1: 철현님 방식 - 뉴 다이스 한 번에 만드는 방식 (내가 방만하게 짠 코드를 한 번 더 정리한 느낌. 깔끔)
# ans type 변경: 디버깅용으로 배열로 해둠 -> 정답 맞췄으니까 효율성을 위해 정수로 바꿈  188 ms -> 196 ms (???? 머쓱)

def roll_dice(dice_dir):
    global dice
    rolled_dice = [[dice[5], dice[1], dice[4], dice[3], dice[0], dice[2]],
                   [dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]],
                   [dice[4], dice[1], dice[5], dice[3], dice[2], dice[0]],
                   [dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]]
    
    dice = rolled_dice[dice_dir]


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
    if dice[0] > arr[dice_y][dice_x]:
        dir_idx = (dir_idx + 1) % 4
    elif dice[0] < arr[dice_y][dice_x]:
        dir_idx = (dir_idx - 1) % 4

print(ans)
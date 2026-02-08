# 각 눈의 상하좌우는 불변값이 아니다. -> 매번 값을 갱신해줘야됨. 미리 매핑테이블을 만들긴 힘들다

#  0,  1, 2, 3, 4, 5
# 아래, 동 서  북  남 위  에 해당하는 현재 값
# 각 인덱스 안에 들어있는 값을 계속 바꿔줄 거임! (인덱스가 곧 방향)
val_of_dice = [0, 0, 0, 0, 0, 0]

# 동 서 북 남 (인덱스 1부터 쓸거임)
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

# 아랫면, 아랫면의 상 하 좌 우, 윗면을 변수로 두고 매번 갱신하면 됨
def roll_dice(cmd):
    bottom = val_of_dice[0]
    east = val_of_dice[1]
    west = val_of_dice[2]
    north = val_of_dice[3]
    south = val_of_dice[4]
    top = val_of_dice[5]

    # 동쪽 ->
    if cmd == 1:
        val_of_dice[0] = east
        val_of_dice[1] = top
        val_of_dice[2] = bottom
        val_of_dice[3] = north
        val_of_dice[4] = south
        val_of_dice[5] = west

    # 서쪽 <-
    elif cmd == 2:
        val_of_dice[0] = west
        val_of_dice[1] = bottom
        val_of_dice[2] = top
        val_of_dice[3] = north
        val_of_dice[4] = south
        val_of_dice[5] = east

    # 북
    elif cmd == 3:
        val_of_dice[0] = north
        val_of_dice[1] = east
        val_of_dice[2] = west
        val_of_dice[3] = top
        val_of_dice[4] = bottom
        val_of_dice[5] = south

    # 남
    elif cmd == 4:
        val_of_dice[0] = south
        val_of_dice[1] = east
        val_of_dice[2] = west
        val_of_dice[3] = bottom
        val_of_dice[4] = top
        val_of_dice[5] = north



# 입력받고, 시작점 찾는다.
N, M, y, x, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move_cmds = list(map(int, input().split()))

ans = []

# 명령을 수행한다
for cmd in move_cmds:
    ny = y + dy[cmd]
    nx = x + dx[cmd]

    if not (0 <= ny < N and 0 <= nx < M):
        continue

    # 그곳으로 이동할 수 있으면 굴린다
    roll_dice(cmd)

    # 이동한 칸에 쓰여 있는 수가 0이 아니면
    if arr[ny][nx] != 0:
        val_of_dice[0] = arr[ny][nx]
        arr[ny][nx] = 0
    # 0이면
    else:
        arr[ny][nx] = val_of_dice[0]

    # 이동 관련한 로직 다 짰으니 좌표 갱신
    y = ny
    x = nx

    ans.append(val_of_dice[5])

for val in ans:
    print(val)
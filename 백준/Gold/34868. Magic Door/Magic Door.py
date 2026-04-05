"""
출력: 모든 과정이 완료된 후 사라진 총 보석의 수

M * N 으로 들어온다는데 나는 N * M 으로 받을래

보석
# 일반 보석
# 폭탄 보석
# 비브라늄 보석

Match-3
# 오직, 일반 보석으로만 구성되어 있어야함 (비브라늄, 폭탄 안됨)
# "셋 이상의 동일한 일반 보석이" 수직 또는 수평 방향으로 연속해 배열된 형태
# 하나의 보석이 서로 교차하는 수평/수직 매치3에 동시에 포함될 수 있다

# 초기 상태의 격자에는 매치3이 없음

# 일반 보석을 두 개 터치하면~~ 돌의 위치가 교환된다.
# 터치할 두 보석의 정보는 입력으로 주어진다.

# 최초 교환 이후, 아래 과정 반복. 더 이상 변화가 없을 때까지
# 1. 연쇄 반응 (반복문)
    # 0. 매치3에 속하는 보석 좌표를 모두 찾는다.
        # match3_coord_set = {}
        # 나부터 오른쪽 탐색하는 거 하나 (방문배열)
        # 나부터 아래 탐색하는 거 하나 (방문배열)
        # 1 이상 9 이하인데, 수가 같고 컴포넌트 len이 >= 3
            # match3_coord_set에 좌표 추가

        => 매치3 하나도 없으면 종료

    # 1. 매치3에 해당하는 모든 보석이 동시에 다 사라진다.
        for y, x in match_coord_set:
            arr[y][x] = BLANK
    # 2. 사라진 보석에 위에 있는 모든 보석이 중력에 의해 낙하해 빈 자리를 메운다.
        # 이때, 폭탄 보석이 한 칸 이상 떨어지면 활성화된다.
    gravity()

# 2. 활성 폭탄 폭파
    # 2-1. 활성 상태에 있는 폭탄이 "동시에" 폭발한다.
        # 그냥 순차적으로 하면 됨, 중력작용 하기 전에
        # 브루트포스로 찾기 640
    for i in range(N):
        for j in range(M):
            if arr[i][j] == ACTIVATED_BOMB:

                arr[i][j] = BLANK
                ans += 1
                for d in range(4):
                    ny = i + dy[d]
                    nx = j + dx[d]

                    # 비브라늄 보석 또는 범위밖 나갈 때까지
                    while inb(ny, nx) and arr[ny][nx] != STRONG_JEWEL:
                        # 활성화된 폭탄은 나중에 또 터트려야 하니까 냅둔다.
                        if arr[ny][nx] != ACTIVATED_BOMB and arr[ny][nx] != BLANK:
                            arr[ny][nx] = BLANK
                            ans += 1

                        ny = ny + dy[d]
                        nx = nx + dx[d]

        # 2. 폭발한 각 폭탄은 수평과 수직 방향으로 광선 방출
            # 비브라늄 보석 또는 범위밖 나갈 때까지
        # 3. 광선의 경로에 있는 모든 일반 보석, 폭탄 보석은 사라진다.
            # 이때 비활성화 폭탄은 더 이상 폭발하지 않고 사라진다.

    # 2-4. 중력 작용. 한 칸 이상 떨어지는 모든 폭탄은 활성화된다.
    gravity()


gravity():
    # 투포인터 형식
    new_arr = [[BLANK] * M for _ in range(N)]

    for x in range(M):
        new_y = N - 1
        for prev_y in range(N - 1, -1, -1):
            if arr[prev_y][x] != BLANK:
                # 비활성화 폭탄인데 한 칸 이상 내려왔다면 활성화
                if arr[prev_y][x] == SLEEPING_BOMB and prev_y != new_y:
                    new_arr[new_y][x] = ACTIVATED_BOMB
                else:
                    new_arr[new_y][x] = arr[prev_y][x]
                new_y -= 1

    return new_arr



시간제한 50'000'000

0은 폭탄 보석
-1은 비브라늄 보석 STRONG_JEWEL
1~9는 일반 보석

0 은 비활성화된 폭탄 보석 SLEEPING_BOMB
-2 는 활성화된 폭탄 보석 ACTIVATED_BOMB
10 은 빈칸 BLANK
"""
"""
테스트케이스
6 4
1 1 2 2
1 2 -1 1
1 1 1 2
1 1 3 1
1 2 2 3
2 1 2 1
6 1 5 4

6 4
1 1 2 2
2 1 -1 1
1 1 1 2
2 1 3 1
1 2 2 3
2 0 0 0
6 1 5 4

6 4
3 3 3 2
3 3 3 1
3 3 3 2
2 1 3 1
1 2 2 3
2 -1 -1 -1
6 1 5 4

6 4
1 1 2 2
3 2 -1 1
3 1 0 0
1 1 3 1
3 2 2 3
2 1 2 1
6 1 5 4

"""

DEBUG = False

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

SLEEPING_BOMB = 0
ACTIVATED_BOMB = -2
STRONG_JEWEL = -1
BLANK = 10


def print_arr():
    if DEBUG:
        print()

        for i in range(N):
            for j in range(M):
                print(f"{arr[i][j]:>2}", end=" ")
            print()

        print()
        print("==================================")


def debug_bp(txt):
    return


def inb(y, x):
    return 0 <= y < N and 0 <= x < M


# TODO: ㄱ, ㅜ, ㄴ 같은 겹친 모양 잘 처리하나 확인 ●
#       2개를 처리하지는 않는지 확인 ●
#       4개 이상도 잘 처리하나 확인: 4개 ● / 5개 ●
#       ...
#       ...
#       ...  => 이런 모양도 잘 처리하나 확인(가로매치3, 세로매치3 다 가능) ●
#       애먼 폭탄보석이나 비브라늄보석, 빈칸으로 매치3 만들진 않는지 확인: 폭탄보석 ● / 비브라늄보석 ● / 빈칸 ●
def find_match3(fdir):
    # 1 이상 9 이하인데, 수가 같고 컴포넌트 len이 >= 3
    # match3_coord_set에 좌표 추가할 set 반환
    visited = [[0] * M for _ in range(N)]
    temp_match3_coord_set = set()
    for i in range(N):
        for j in range(M):
            if 0 < arr[i][j] <= 9 and not visited[i][j]:

                now_match3_candidate_lst = [(i, j)]
                visited[i][j] = 1

                ny = i + dy[fdir]
                nx = j + dx[fdir]

                while True:
                    if not inb(ny, nx): break
                    if visited[ny][nx]: break
                    if arr[ny][nx] != arr[i][j]: break

                    now_match3_candidate_lst.append((ny, nx))
                    visited[ny][nx] = 1
                    ny = ny + dy[fdir]
                    nx = nx + dx[fdir]

                if len(now_match3_candidate_lst) >= 3:
                    temp_match3_coord_set.update(now_match3_candidate_lst)

    debug_bp("매치3 탐색 함수 잘 되나 확인")
    return temp_match3_coord_set


# TODO: 한 칸만 움직인 비활성화 폭탄이 활성화 폭탄 되는지 ●
#       한 칸도 안 움직인 비활성화 폭탄은 여전히 비활성화 폭탄인지 ●
def gravity():
    # 투포인터 형식
    new_arr = [[BLANK] * M for _ in range(N)]

    for x in range(M):
        new_y = N - 1
        for prev_y in range(N - 1, -1, -1):
            if arr[prev_y][x] != BLANK:
                # 비활성화 폭탄인데 한 칸 이상 내려왔다면 활성화
                if arr[prev_y][x] == SLEEPING_BOMB and prev_y != new_y:
                    new_arr[new_y][x] = ACTIVATED_BOMB
                else:
                    new_arr[new_y][x] = arr[prev_y][x]
                new_y -= 1

    return new_arr

# TODO: 폭탄 여러 개 터질 때도 잘 되나 확인 ●
def explode_activate_bombs():
    now_ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == ACTIVATED_BOMB:

                arr[i][j] = BLANK
                now_ans += 1
                for d in range(4):
                    ny = i + dy[d]
                    nx = j + dx[d]

                    # 비브라늄 보석 또는 범위밖 나갈 때까지
                    while inb(ny, nx) and arr[ny][nx] != STRONG_JEWEL:
                        # 활성화된 폭탄은 나중에 또 터트려야 하니까 냅둔다.
                        if arr[ny][nx] != ACTIVATED_BOMB and arr[ny][nx] != BLANK:
                            arr[ny][nx] = BLANK
                            now_ans += 1

                        ny = ny + dy[d]
                        nx = nx + dx[d]

    return now_ans


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sy1, sx1, sy2, sx2 = map(int, input().split())  # 1-indexed로 주어짐
ans = 0

# 0. 바꾸라는 보석 두 개 바꾼다.
arr[sy1 - 1][sx1 - 1], arr[sy2 - 1][sx2 - 1] = arr[sy2 - 1][sx2 - 1], arr[sy1 - 1][sx1 - 1]

debug_bp("자료구조 생성 완료")

while True:
    # 0. 과정 종료 확인용으로... 기존 arr를 복사해둔다.
    prev_arr = [row[:] for row in arr]

    # 1. 연쇄 반응 (반복문)
    while True:
        # 1-1. 매치3에 속하는 보석 좌표를 모두 찾는다.
        match3_coord_set = set()
        match3_coord_set.update(find_match3(1)) # 아래로 탐색
        debug_bp("아래 탐색 완료")
        match3_coord_set.update(find_match3(3)) # 오른쪽으로 탐색
        debug_bp("오른쪽 탐색 완료")

        # 터트릴 게 하나도 없으면 종료
        if not match3_coord_set:
            break

        # 1-2. 매치3에 해당하는 모든 보석이 동시에 다 사라진다.
        ans += len(match3_coord_set)
        for y, x in match3_coord_set:
            arr[y][x] = BLANK
        print_arr()
        debug_bp("1-2. 매치3 터트린 배열")

        # 1-3. 사라진 보석에 위에 있는 모든 보석이 중력에 의해 낙하해 빈 자리를 메운다.
        # 이때, 폭탄 보석이 한 칸 이상 떨어지면 활성화된다.
        arr = gravity()
        print_arr()
        debug_bp("1-3. 중력 작용")

    # 2. 활성 폭탄 폭파
    # 2-1. 활성 상태에 있는 폭탄이 "동시에" 폭발한다.
        # 그냥 순차적으로 하면 됨, 중력작용 하기 전에
        # 브루트포스로 찾기 640
    ans += explode_activate_bombs()
    debug_bp("2-1. 활성 폭탄 폭파")
    print_arr()

    # 2-2. 중력 작용. 한 칸 이상 떨어지는 모든 폭탄은 활성화된다.
    arr = gravity()
    print_arr()
    debug_bp("2-1. 중력 작용")

    # 3. 종료되나 확인
    if arr == prev_arr:
        break

print(ans)

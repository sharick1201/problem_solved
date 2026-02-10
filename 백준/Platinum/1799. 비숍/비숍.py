
# 흑판과 백판은 서로 겹치지 않는 대각선 집합이라 따로 백트래킹을 수행 가능
# 그러면 2 ** N 이 2 ** (N//2) * 2 로 대폭 줄어듦 놀라움~~

def backtracking_black(depth, cnt):
    global ans_black

    # 가지치기
    # 처음에 이 조건 잘못 적어서 틀렸당
    if cnt + (len(black_pos) - depth) <= ans_black:
        return

    if depth == len(black_pos):
        ans_black = max(ans_black, cnt)
        return

    i, j = black_pos[depth]

    # 그 자리에 대해서
    # 놓을 수 있으면 놓아보는 경우
    if arr[i][j] == 1 and visited_lud_black[i + j] and visited_rud_black[i - j + (N - 1)]:
        visited_lud_black[i + j] = 0
        visited_rud_black[i - j + (N - 1)] = 0

        backtracking_black(depth + 1, cnt + 1)

        visited_lud_black[i + j] = 1
        visited_rud_black[i - j + (N - 1)] = 1

    # 놓지 않는 경우
    backtracking_black(depth + 1, cnt)

def backtracking_white(depth, cnt):
    global ans_white

    # 가지치기
    if cnt + (len(white_pos) - depth) <= ans_white:
        return

    if depth == len(white_pos):
        ans_white = max(ans_white, cnt)
        return

    i, j = white_pos[depth]

    # 그 자리에 대해서
    # 놓을 수 있으면 놓아보는 경우
    if arr[i][j] == 1 and visited_lud_white[i + j] and visited_rud_white[i - j + (N - 1)]:
        visited_lud_white[i + j] = 0
        visited_rud_white[i - j + (N - 1)] = 0

        backtracking_white(depth + 1, cnt + 1)

        visited_lud_white[i + j] = 1
        visited_rud_white[i - j + (N - 1)] = 1

    # 놓지 않는 경우
    backtracking_white(depth + 1, cnt)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 사용가능한 흑판과 백판 위치 저장
black_pos = []
white_pos = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            if (i + j) % 2 == 0:
                black_pos.append((i, j))
            else:
                white_pos.append((i, j))

# 각각의 대각선 방문 체크 배열
# 흑판용
visited_lud_black = [1] * (2 * N - 1)
visited_rud_black = [1] * (2 * N - 1)
# 백판용
visited_lud_white = [1] * (2 * N - 1)
visited_rud_white = [1] * (2 * N - 1)

# 각각의 최대값
ans_black = 0
ans_white = 0

backtracking_black(0, 0)
backtracking_white(0, 0)

# 최종 답은 두 결과를 더하면 됨
print(ans_black + ans_white)


from collections import deque


BLANK = -3
BLACK = -1
RAINBOW = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx, color):
    global visited, group_info_lst, group_yx_lst

    # 필요한 자료구조 생성
    q = deque()

    comp_lst = []              # 이 컴포넌트에 해당하는 좌표들
    base_y, base_x = -1, -1    # 기준블록
    rainbow_lst = []           # 무지개 좌표들

    # 초기값 할당
    comp_lst.append((sy, sx))
    q.append((sy, sx))
    visited[sy][sx] = True
    base_y, base_x = sy, sx

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            ### 더 이상 가지 않는 경우 ###
            # 범위밖
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            # BLANK, BLACK
            if arr[ny][nx] == BLACK or arr[ny][nx] == BLANK:
                continue
            # 그 색깔인데 이미 방문
            if arr[ny][nx] == color and visited[ny][nx]:
                continue

            ### 가는 경우 ###
            # 그 색깔인데 아직 미방문
            if arr[ny][nx] == color and not visited[ny][nx]:
                # base_y, base_x 갱신
                if base_y > ny:
                    base_y, base_x = ny, nx
                elif base_y == ny and base_x > nx:
                    base_y, base_x = ny, nx

                # 방문 처리
                visited[ny][nx] = True

                # q에 넣기
                q.append((ny, nx))
                # comp_lst에 추가
                comp_lst.append((ny, nx))


            # 무지개인데 아직 미방문
            if arr[ny][nx] == RAINBOW and not visited[ny][nx]:
                # 무지개 리스트에 추가
                rainbow_lst.append((ny, nx))

                # 방문 처리
                visited[ny][nx] = True

                # q에 넣기
                q.append((ny, nx))
                # comp_lst에 추가
                comp_lst.append((ny, nx))


    # 컴포넌트 다 만들었으니 lst에 할당

    # 블록 그룹이 아니면 뭐 더 하지 않는다.
    if len(comp_lst) == 1:
        # visited[sy][sx] = False 안해줘도 됨 어차피 외딴섬이니까
        return

    # group_info_lst에 추가
    group_info_lst.append((len(comp_lst), len(rainbow_lst), base_y, base_x, len(group_info_lst)))   # (컴포넌트 크기, 무지개수, y, x, 블록인덱스)

    # group_yx_lst에 추가
    group_yx_lst.append(comp_lst)

    # 이때 무지게 리스트에 있는 것들은 다시 visited = False 로 해둬야 컴포넌트 만들 때 재사용 가능
    for y, x in rainbow_lst:
        visited[y][x] = False



# # 중력작용
def gravity():

    for x in range(N):
        for y in range(N-2, -1, -1):

            # BLACK은 중력작용 안 받음
            if arr[y][x] == BLACK:
                continue

            # arr[y][x] 에 대하여, 중력작용. ny로 갈 수 있는지 확인한다.
            ny = y + 1
            while 0 <= ny < N:
                # 만약 다른 블록이 있으면
                if arr[ny][x] != BLANK:
                    break

                # 빈칸이면 swap하고, 한 칸 더 내려가본다.
                arr[ny][x], arr[ny-1][x] = arr[ny-1][x], arr[ny][x]
                ny += 1



# arr를 반시계방향으로 회전
def rotate_arr():
    global arr
    # 전치 후 상하반전
    temp = list(map(list, zip(*arr)))
    temp = temp[::-1]
    # 다시 arr에 temp 할당
    arr = [row[:] for row in temp]



""" 입력 """
N, color_N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0


""" 시뮬레이션 """
while True:
    # 1-1. 크기가 큰 블록 그룹들을 만든다.
    visited = [[False] * N for _ in range(N)] # 방문처리용
    group_info_lst = [] # (블록수, 무지개수, y, x, 블록인덱스)
    group_yx_lst = []   # [블록인덱스] = 그 블록그룹에 포함되는 블록들의 좌표

    for i in range(N):
        for j in range(N):
            # 자연수고, not visited면 ㄱㄱ
            if arr[i][j] > 0 and not visited[i][j]:
                bfs(i, j, arr[i][j])

    # 1-1. 가장 큰 그룹을 뽑는다. 이때 그룹이 하나도 없으면 종료
        # 후보 리스트를 안 만들고, 그냥 최대그룹을 매번 갱신하는 방식도 있는데 디버깅 쉬우라고 리스트 만듦
    if not group_info_lst:
        break

    else:
        group_info_lst.sort(reverse=True)
        biggest_group_size, _, _, _, biggest_group_idx = group_info_lst[0]


    # 2. 1에서 찾은 블록 그룹의 모든 블록을 제거하고, 점수를 계산한다
    # 모든 블록 제거
    for y, x in group_yx_lst[biggest_group_idx]:
        arr[y][x] = BLANK

    # 점수계산
    ans += biggest_group_size ** 2

    # print_arr()

    # 3. 격자 중력 작용
    gravity()
    # print_arr()

    # 4. 반시계방향으로 회전
    rotate_arr()
    # print_arr()

    # 5. 격자 중력 작용
    gravity()
    # print_arr()


""" 시뮬레이션 종료, 정답 출력 """
print(ans)
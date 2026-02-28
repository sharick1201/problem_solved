"""
출력: 학생 만족도의 총 "합"

N x N 정사각형 (N <= 20)
가장 윗칸  1, 1

인접하다 = 상, 하, 좌, 우

각 학생에 대하여,
1. 빈 칸 중에서, 상하좌우 체크 -> 좋아하는 학생 있으면 카운트 -> 카운트 가장 큰 빈칸에 앉힌다.
2. max(카운트) 가 여러 개라면(1을 만족하는 칸이 여러개라면) 인접한 칸 중에 비어있는 칸이 가장 많은 칸으로 자리 정한다
3. 2를 만족하는 칸도 여러 개인 경우, 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로.

모두 다 앉혔으면
for i in range(N):
    for j in range(N):
        상하좌우 체크해서 만족도 누적
        친한친구 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
"""

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())
arr = [[0] * N for _ in range(N)]

# idx 학생번호 / val: 좋아하는 학생 번호 4개가 있는 set
# 1번 인덱스부터 사용
fav_lst = [[] for _ in range(N**2 + 1)]
ans = 0   # 학생 만족도


# stu_idx를 앉힐거임
for _ in range(N**2):
    stu_idx, fav1, fav2, fav3, fav4 = map(int, input().split())
    fav_lst[stu_idx] = {fav1, fav2, fav3, fav4}

    candidates = []  # [최애카운트, 빈칸카운트, y, x]

    for i in range(N):
        for j in range(N):
            # 각 빈칸(0)에 대해, stu_idx가 앉을 수 있는 후보 자리들을 찾는다.
            if arr[i][j] == 0:
                fav_cnt = 0     # 최애 카운트
                empty_cnt = 0   # 빈 칸 카운트

                for d in range(4):
                    ny = i + dy[d]
                    nx = j + dx[d]
                    if not (0 <= ny < N and 0 <= nx < N):
                        continue
                    # 최애 있는지 없는지 - 빈자리인지 아닌지 => 배타적이다. (둘 다 만족하는 자리는 없음)
                    # 빈자리면
                    if arr[ny][nx] == 0:
                        empty_cnt += 1
                    elif arr[ny][nx] in fav_lst[stu_idx]:
                        fav_cnt += 1

                # cnt 둘 다 0이라도 무조건 다 리스트에 집어넣어야됨. (항상 happy할 수 없다...)
                candidates.append([fav_cnt, empty_cnt, i, j])

    # 정렬하면 됨: [0] [1] 은 내림차순, [2] [3] 은 오름차순으로
    candidates.sort(key=lambda val: (4-val[0], 4-val[1], val[2], val[3]))

    # 후보가 하나도 없는 경우는 없을텐디... 혹시 모르니 문제 생기면 체크
    # best 자리는 정렬 후의 0번째 자리
    best_y, best_x = candidates[0][2], candidates[0][3]

    # 확정
    arr[best_y][best_x] = stu_idx


for i in range(N):
    for j in range(N):
        # arr[i][j] 에 대해, 인접한 곳에 있는 최애학생 수 체크
        cnt = 0
        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if arr[ny][nx] in fav_lst[arr[i][j]]:
                cnt += 1

        # 값 계산
        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000
        # cnt == 0 이면 만족도 변화 없음

print(ans)
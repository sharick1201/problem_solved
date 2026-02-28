"""
출력: 이동 K번 완료 후, 남아있는 파이어볼 "질량의 합"

N*N
1, 1 => 0, 0 으로 바꿔주기
1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.

아래 일들이 K번 이루어진다

1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    2. 파이어볼은 4개의 파이어볼로 나누어진다.
    3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.   -> 이거 반올림이었던가??? 와 개에바 걍 개무식이슈;;;;; 내림인듯
        속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
    4. 질량이 0인 파이어볼은 소멸되어 없어진다.
"""


""" 입력받으면서 필요판 자료구조 생성 """
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


N, M, K = map(int, input().split())

# [y][x] 에 있는 파이어볼들 [질량, 속력, 방향 순]
arr = [[[] * N for _ in range(N)] for _ in range(N)]

# 0. 초기 파이어볼 위치 할당
for _ in range(M):
    y, x, fw, fs, fd = map(int, input().split())
    arr[y-1][x-1].append([fw, fs, fd])   # 질량, 속력, 방향 순

""" 시뮬레이션 """

for _ in range(K):
    new_arr = [[[] * N for _ in range(N)] for _ in range(N)]

    # 1. 모든 파이어볼을 이동시킨다.
    for i in range(N):
        for j in range(N):
            for fw, fs, fd in arr[i][j]:
                new_arr[(i + fs * dy[fd]) % N][(j + fs * dx[fd]) % N].append([fw, fs, fd])

    # print("end of phase1")
    # arr 판 비우고 거기 갱신
    arr = [[[] * N for _ in range(N)] for _ in range(N)]

    # 2. 2개 이상의 파이어볼이 있는 칸에서의 변화 ㄱㄱ
    for i in range(N):
        for j in range(N):

            # 1개면 그냥 그 자리에 갱신!
            if len(new_arr[i][j]) == 1:
                arr[i][j].append([new_arr[i][j][0][0], new_arr[i][j][0][1], new_arr[i][j][0][2]])

            elif len(new_arr[i][j]) >= 2:
                # 파이어볼을 합쳐서 새로운 파이어볼을 만든다
                new_fw = 0  # 질량
                new_fs = 0  # 속력
                new_fd = []  # 방향
                f_cnt = len(new_arr[i][j])  # 파이어볼 갯수

                for fw, fs, fd in new_arr[i][j]:
                    new_fw += fw
                    new_fs += fs
                    new_fd.append(fd)

                # 새 파이어볼 값 계산
                # new_fw = int((new_fw / 5 + 0.5) * 10 // 10)
                new_fw = new_fw // 5
                # new_fs = int((new_fs / f_cnt + 0.5) * 10 // 10)
                new_fs = new_fs // f_cnt
                # 모두 짝수거나 홀수면
                if all(new_fd[x] % 2 == 0 for x in range(f_cnt)) or all(new_fd[x] % 2 == 1 for x in range(f_cnt)):
                    new_fd = [0, 2, 4, 6]
                else:
                    new_fd = [1, 3, 5, 7]

                # 새파이어볼 ㄱㄱ (근데 질량이 0이면 나가리)
                if new_fw > 0:
                    for d in range(4):
                        # 질량, 속력, 방향
                        arr[i][j].append([new_fw, new_fs, new_fd[d]])

    # print("end of phase2")

ans = 0
""" 정답 카운트 """
for i in range(N):
    for j in range(N):
        for fw, fs, fd in arr[i][j]:
            ans += fw

print(ans)
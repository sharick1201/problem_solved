"""
출력: 모든 막대를 던지고 난 이후의 미네랄 모양

미네랄: x
클러스터: 미네랄의 컴포넌트

창영: 동굴 왼쪽 (0열에서부터 쭈욱 던짐
상근: 동굴 오른쪽 (M-1열에서부터 슝
번갈아가면서 막대기 던진다. 어떻게? 행과 수평하여. 높이는? 1이면 N-1 번째 행. N 이면 0 번째 행
    => 막대기가 가다가 미네랄 만나면 그거 파괴시키고 막대기 이동 종료


cmd_N 만큼 아래 과정 반복
1. 막대기 던짐
    - 던지다가 미네랄 만나면 파괴, 막대기 이동 종료
    - 안 만나면 그냥 막대기 던진 사람 됨

2. 미네랄 만나서 파괴되었다면...
    - 미네랄 중력작용
"""

# 미네랄과 다른 점:
# 클러스터가 떨어질 때, 그 클러스터 각 열의 맨 아래 부분 중 하나가 바닥 또는 미네랄 위로 떨어지는 입력만 주어진다는 말이 없음
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 클러스터 세기
def cnt_clusters():
    global clusters
    clusters = [[0] * M for _ in range(N)]
    cluster_num = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'x' and clusters[i][j] == 0:
                clusters[i][j] = cluster_num
                q = deque()
                q.append((i, j))

                while q:
                    y, x = q.popleft()

                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if not (0 <= ny < N and 0 <= nx < M): continue
                        if not arr[ny][nx] == 'x': continue
                        if not clusters[ny][nx] == 0: continue

                        clusters[ny][nx] = cluster_num
                        q.append((ny, nx))
                cluster_num += 1


# phase 2
# 미네랄이 파괴되었을 때 호출됨. 중력작용
# return 없음
def gravity(cluster_num):
    cluster_cells = [(i, j) for i in range(N) for j in range(M)
                     if clusters[i][j] == cluster_num]

    if not cluster_cells: return

    cluster_set = set(cluster_cells)

    min_drop = N
    for y, x in cluster_cells:
        drop = 0
        ny = y + 1
        # 클러스터 자신의 셀은 건너뜀
        while ny < N and (arr[ny][x] == '.' or (ny, x) in cluster_set):
            drop += 1
            ny += 1
        min_drop = min(min_drop, drop)

    if min_drop == 0:
        return

    for y, x in sorted(cluster_cells, key=lambda c: -c[0]):
        arr[y + min_drop][x] = 'x'
        arr[y][x] = '.'



# phase 1
# 막대기를 던지고, 미네랄 파괴. 미네랄 파괴되었다면 중력작용 함수 호출
# return 없음
def throw_stick(frm, to, how, cmd):
    for i in range(frm, to, how):
        if arr[N - cmd][i] == 'x':
            # 1. 미네랄 파괴
            arr[N - cmd][i] = '.'
            # 2. 클러스터 계산
            cnt_clusters()
            # 3. 인접 클러스터에 중력작용
            for d in range(4):
                ny = N - cmd + dy[d]
                nx = i + dx[d]
                if not(0 <= ny < N and 0 <= nx < M): continue
                if clusters[ny][nx] == 0: continue
                gravity(clusters[ny][nx])
            break

######################################################
""" 입력받기 """
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
cmd_N = int(input())
cmds = list(map(int, input().split()))

clusters = [[0] * M for _ in range(N)]

""" 명령 단위 시뮬레이션 """
for idx, cmd in enumerate(cmds):
    # 창영 턴이면
    if idx % 2 == 0:
        throw_stick(0, M, 1, cmd)
    # 상근 턴이면
    else:
        throw_stick(M-1, -1, -1, cmd)

""" 시뮬레이션 종료 후 출력 """
for i in range(N):
    print("".join(arr[i]))
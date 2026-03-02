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

    col_bottom = {}
    for y, x in cluster_cells:
        col_bottom[x] = max(col_bottom.get(x, 0), y)

    min_drop = N
    for x, bottom_y in col_bottom.items():
        drop = 0
        ny = bottom_y + 1
        while ny < N and arr[ny][x] == '.':
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
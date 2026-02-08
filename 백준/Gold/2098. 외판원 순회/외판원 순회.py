
# N이 16까지 !
# 외판원 순회 2 처럼 하면 시간초과

# dp + 비트마스킹 + 백트래킹 이거마즘???? 이렇게까지풀어야한다고?
# 너무너무너무너무너무너무너무힘든싸움이엇다...

# 직전코드랑 바뀐 거 매번 int(1e9) 인거 변수로만 바꿨는데 될까? -> 안됨
# 백트래킹에서 이미 방문 완료했는데 불가능한 경우도 INF, 초기값도 INF라 불가능한 경우를 여러 번 탐색하게 되어 시간초과나는듯...?
# 개끔찍문제;;
INF = int(1e9)

def backtracking(prev, visited_bit):

    # 종료조건 1 (모두 방문했으면)
    if visited_bit == 2 ** N - 1:
        # 시작점으로 돌아가는게 가능한지도 체크해야됨
        if arr[prev][0] != 0:
            # 시작점으로 돌아가는 비용
            return arr[prev][0]
        # 시작점으로 못가면
        else:
            return INF

    # 종료조건 2 (이미 그 DP값 계산했으면)
    if DP[prev][visited_bit] != -1:
        return DP[prev][visited_bit]


    # 아래 for문 돌았는데 한 번도 min 계산 못했으면 더 이상 진행이 불가하다는 뜻이므로 INF 할당해두기
    DP[prev][visited_bit] = INF

    # 점화식 기반으로 DP 테이블을 채우자
    for nxt in range(1, N):
        # i번째 집 이미 방문했으면
        if visited_bit & (1 << nxt):
            continue

        # 방문 불가하면
        if arr[prev][nxt] == 0:
            continue

        DP[prev][visited_bit] = min(DP[prev][visited_bit], backtracking(nxt, visited_bit | 1 << nxt) + arr[prev][nxt])

    return DP[prev][visited_bit]




# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# [prev][visited] visited는 비트로 표시
# 그 prev 에, 그 visited에 있어서 최소값
######################################
# [수정]
# 이 아니라... 그 prev 에, 그 visited에 있어서 앞으로 남은 곳을 모두 방문했을 때 최단 경로값
# DP[prev][visited] = min(DP[prev][visited], DP[nxt][visited | 1 << nxt] + arr[prev][nxt])
# 방문해봤는데 불가능하다 -> INF / 아직 방문안했다 -> -1 로

# 사이클이 있는 그래프라 시작점을 어디로 상정하든 괜찮음
# 난 0으로 할래
DP = [[-1] * (2 ** N) for _ in range(N)]

# 시작점 0으로 두자
ans = backtracking(0, 0b1)

print(ans)
from heapq import heappop, heappush
# 랜선 길이가 가중치인 MST 문제
# MST를 만들고, 랜선 길이의 합에서 그 MST 가중치의 합을 빼면 됨

def prim(start_v):
    visited = [False] * N
    pq = []
    heappush(pq, (0, start_v))

    ans = 0  # MST 가중치
    cnt = 0  # 확정된 정점

    while pq:
        now_w, now_v = heappop(pq)

        if visited[now_v]:
            continue

        visited[now_v] = True
        ans += now_w
        cnt += 1

        # 모든 정점이 연결되어 있으면
        if cnt == N:
            return ans

        # 다음 후보 찾기
        for nxt_v in range(N):
            if visited[nxt_v]:
                continue
            # 어떻게도 못 가면
            if adj_mat[now_v][nxt_v] == 0 and adj_mat[nxt_v][now_v] == 0:
                continue
            # 둘 중 하나만 있으면
            if adj_mat[now_v][nxt_v] == 0:
                heappush(pq, (adj_mat[nxt_v][now_v], nxt_v))
            elif adj_mat[nxt_v][now_v] == 0:
                heappush(pq, (adj_mat[now_v][nxt_v], nxt_v))
            # 둘 다 있으면
            else:
                heappush(pq, (min(adj_mat[nxt_v][now_v], adj_mat[now_v][nxt_v]), nxt_v))


    return -1


N = int(input())
origin_arr = list(input() for _ in range(N))

# 보기 편한 숫자로 바꾸자
adj_mat = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if origin_arr[i][j] == '0':
            adj_mat[i][j] = 0
        elif 'a' <= origin_arr[i][j] <= 'z':
            adj_mat[i][j] = ord(origin_arr[i][j]) - ord('a') + 1
        elif 'A' <= origin_arr[i][j] <= 'Z':
            adj_mat[i][j] = ord(origin_arr[i][j]) - ord('A') + 27
        # else인 경우는 없다


# 어디서 시작하든 상관없다
result = prim(0)

# 모든 컴퓨터가 연결되어 있지 않은 경우는 -1
if result == -1:
    print(-1)
else:
    sm = 0
    for i in range(N):
        sm += sum(adj_mat[i])

    print(sm - result)
N1, M1 = map(int, input().split())
arr1 = list(list(input()) for _ in range(N1))
N2, M2 = map(int, input().split())
arr2 = list(list(input()) for _ in range(N2))

coin_cnt = sum(arr1[i].count('O') for i in range(N1))
max_overlap_cnt = 0

# 다른 사람들처럼 그리드 만들어서 해보기
# N = (N2 - 1) + N1 + (N2 - 1)
N = 2 * N2 + N1 - 2
M = 2 * M2 + M1 - 2
grid = [['.'] * M for _ in range(N)]

# 중앙에 arr1 집어넣기
for i in range(N1):
    for j in range(M1):
        grid[i + N2 - 1][j + M2 - 1] = arr1[i][j]

# arr2 이동시켜가면서 해보기
for si in range(N):
    for sj in range(M):
        cnt = 0

        # 이동된 lst2 <-> lst1 비교하면서 동전 겹치는 부분 카운트
        for i in range(N2):
            for j in range(M2):
                ny = i + si
                nx = j + sj
                if not (0 <= ny < N and 0 <= nx < M):
                    continue
                if grid[ny][nx] == 'O' and arr2[i][j] == 'O':
                    cnt += 1

        max_overlap_cnt = max(max_overlap_cnt, cnt)

print(coin_cnt - max_overlap_cnt)
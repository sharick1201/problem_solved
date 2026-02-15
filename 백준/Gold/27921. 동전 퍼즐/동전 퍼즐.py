N1, M1 = map(int, input().split())
arr1 = list(input() for _ in range(N1))
N2, M2 = map(int, input().split())
arr2 = list(input() for _ in range(N2))

N = max(N1, N2)
M = max(M1, M2)

coin_cnt = sum(arr1[i].count('O') for i in range(N1))
max_overlap_cnt = 0


for diff_i in range(-N+1, N):
    for diff_j in range(-M+1, M):

        cnt = 0

        # 이동된 lst2 <-> lst1 비교하면서 동전 겹치는 부분 카운트
        for i in range(N1):
            for j in range(M1):
                ny = i + diff_i
                nx = j + diff_j
                if not (0 <= ny < N2 and 0 <= nx < M2):
                    continue
                if arr1[i][j] == 'O' and arr2[ny][nx] == 'O':
                    cnt += 1

        max_overlap_cnt = max(max_overlap_cnt, cnt)

print(coin_cnt - max_overlap_cnt)

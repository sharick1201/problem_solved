T = int(input())
for _ in range(T):
    N = int(input())
    # 학생들의 선택 (1-indexed)
    choices = [0] + list(map(int, input().split()))

    #  0이면 미방문, 그 외 시작노드
    visited = [0] * (N + 1)
    team_member_cnt = 0

    for i in range(1, N + 1):
        if visited[i] == 0:
            curr = i
            path = []

            # 미방문 노드만
            while visited[curr] == 0:
                visited[curr] = i  # 이번 탐색의 시작 노드 번호로 방문 표시
                path.append(curr)
                curr = choices[curr]

            # 마주친 노드의 방문값이 '이번 탐색의 시작 노드 번호'면... 사이클!
            if visited[curr] == i:
                # path에서 curr이 등장한 위치부터 사이클
                cycle_start_idx = path.index(curr)
                team_member_cnt += len(path) - cycle_start_idx

    print(N - team_member_cnt)
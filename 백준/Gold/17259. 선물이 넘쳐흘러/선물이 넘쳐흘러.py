'''
[주의사항]
- 바로 앞 벨트 것만 하는 거 아님. 인접한 칸에서 일한다. (2개 이상일 수 있음)
- 인접한 선물이 2개 이상이라면, 벨트 위에 더 오래 올려져 있던 선물을 포장한다.

[자료구조 선정]
- 공장: 공장 2차원 배열 있는게 속편할듯 최대 100 x 100밖에 안되기도 하고
    - True: 포장 안 한 선물
- 직원: [y, x, 포장 완료까지 남은 시간] 이 M개 있는 2차원 리스트
    - 벨트 위에 더 오래 올려져 있던 선물: 하, 우, 상 순으로 체크하면 됨(좌에 선물이 오는 경우는 없음)

[큰 틀]
- 초 단위로 이동하며 시뮬레이션. 마지막 선물이 그리드 바깥으로 나가면(B * 3 - 2 + M초까지) 종료
각 초가 시작되면
1. 컨베이어 벨트를 이동시킨다 (이 과정에서 첫 칸에 선물을 하나 더 둔다. 폐기되는 선물은 none of my business...)
2. 각 직원이 포장 중이면 완료까지 남은 시간에 -1초.
3. 각 idx번 직원에 대해 포장할 수 있는지 체크
    - 포장할 수 있으면 ([idx][2] == 0 이면) 바로 포장 ㄱㄱ
        - 포장한 선물 cnt +1
        - labor_time[idx] 시간만큼 [idx][2] 할당하고, 그리드에서 1을 0으로 바꾼다.
    - 못하면 냅둬
'''
dy = [1, 0, -1]
dx = [0, 1, 0]


# 첫 칸에 선물 둠 + 컨베이어 벨트를 이동시키는 함수.
# return 안함
def move_belt():
    global remaining_present_cnt
    # 끝지점부터 역순으로 ㄱㄱ
    for j in range(B-1):
        grid[B-1][j] = grid[B-1][j+1]

    for i in range(B-1, 0, -1):
        grid[i][B-1] = grid[i-1][B-1]

    for j in range(B-1, 0, -1):
        grid[0][j] = grid[0][j-1]

    # 첫 자리에 선물을 두자. 아직 안 컨베이어 벨트에 안 올린 선물이 있을 때만
    if remaining_present_cnt > 0:
        # 첫 자리에 선물 두기
        grid[0][0] = True
        remaining_present_cnt -= 1
    else:
        grid[0][0] = False


""" 0. 입력받기 + 필요한 자료구조 만들기 """
B, N, M = map(int, input().split())

grid = [[False] * B for _ in range(B)] # 공장
labor_time = []    # idx번 직원이 포장하는 데에 소요되는 시간
employee_lst = []  # idx번 직원의 [y, x, 포장 완료까지 남은 시간]

remaining_present_cnt = M   # 아직 컨베이어벨트에 안 올라간 선물 갯수
packaged_present_cnt = 0    # 포장한 선물 갯수

for i in range(N):
    y, x, t = map(int, input().split())
    labor_time.append(t)
    employee_lst.append([y, x, 0])

""" 1. 초 단위 시뮬레이션 """
for t in range(B * 3 - 2 + M):
    # 1. 컨베이어 벨트 이동
    move_belt()

    for i in range(len(employee_lst)):
        # 2. 각 직원이 포장 중이면 완료까지 남은 시간에 -1초
        if employee_lst[i][2] > 0:
            employee_lst[i][2] -= 1

        # 3. 각 idx번 직원에 대해 포장할 수 있는지 체크
        # 주변에 선물이 있고 / 그 직원 포장 가능하면 포장 ㄱㄱ
        if employee_lst[i][2] == 0:
            for j in range(3):
                ny = employee_lst[i][0] + dy[j]
                nx = employee_lst[i][1] + dx[j]

                if not (0 <= ny < B and 0 <= nx < B):
                    continue

                if grid[ny][nx]:
                    packaged_present_cnt += 1
                    employee_lst[i][2] = labor_time[i]
                    grid[ny][nx] = False

                    break

""" 2. 출력 """
print(packaged_present_cnt)

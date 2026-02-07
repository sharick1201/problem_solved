# 좌표 간 거리 구하는 함수
def cal_dis(chicken_idx, house_idx):
    return abs(chicken[chicken_idx][0] - house[house_idx][0]) + abs(chicken[chicken_idx][1] - house[house_idx][1])


# 치킨 거리 구하는 함수
def cal_chicken_dist():
    sm = 0

    # 각 집에 대해서 가장 가까운 치킨집 선정해서 합한다
    for i in range(house_length):
        temp = 50 ** 2
        for j in picked_chickens:
            temp = min(mapping_table[j][i], temp)
        sm += temp

    return sm


# 원소 수가 M인 치킨집 조합 구하는 함수
def backtracking(depth, prev):
    global ans

    # 종료조건
    if depth == M:
        # 치킨 거리 계산
        ans = min(cal_chicken_dist(), ans)
        return

    for i in range(prev + 1, chicken_length):
        picked_chickens.append(i)
        backtracking(depth + 1, i)
        picked_chickens.pop()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 0이면 빈칸, 1이면 집, 2이면 치킨집

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

chicken_length = len(chicken)
house_length = len(house)
# 각 치킨집 - 각 집까지의 거리를 저장하는 테이블을 생성한다
# y: 치킨집 idx
# x: 집 idx
mapping_table = [[-1] * house_length for _ in range(chicken_length)]

for i in range(chicken_length):
    for j in range(house_length):
        mapping_table[i][j] = cal_dis(i, j)


# 살릴 치킨집 조합을 구하고, 그 조합들에 대해 치킨 거리 계산
ans = 100 * 20
picked_chickens = []   # 살릴 치킨집들의 인덱스
backtracking(0, -1)

print(ans)
DEBUG = False


def print_debug(args):
    if DEBUG:
        print(*args)


def rotate_90(arr):
    return [row[::-1] for row in list(map(list, zip(*arr)))]


def add_fish_first():
    # 이 함수가 호출될 땐 항상 1차원 배열
    min_val = min(fishbowl)
    for i in range(N):
        if fishbowl[i] == min_val:
            fishbowl[i] += 1


# 1차원 -> 2차원
def update_fishbowl():
    global fishbowl

    # 처음 1개를 오른쪽 위로 올린다.
    fishbowl = [fishbowl[:1]] + [fishbowl[1:]]

    while True:
        sero = len(fishbowl)          # 현재 쌓인 블록 높이
        garo = len(fishbowl[0])       # 현재 쌓인 블록 너비
        remain = len(fishbowl[-1]) - garo   # 오른쪽 바닥에 남은 길이

        # 회전 후 너비는 sero가 되니까 남은 바닥 길이가 sero 이상이어야 올릴 수 있다.
        if remain < sero:
            break

        temp = [row[:garo] for row in fishbowl]   # 왼쪽 쌓인 블록
        temp = rotate_90(temp)

        fishbowl = temp + [fishbowl[-1][garo:]]


# 2차원 배열
def adjust_fish_num():
    global fishbowl

    new_arr = [row[:] for row in fishbowl]

    for i in range(len(fishbowl)):
        for j in range(len(fishbowl[i])):
            for dy, dx in [(0, 1), (1, 0)]:
                ni, nj = i + dy, j + dx

                if ni < len(fishbowl) and nj < len(fishbowl[i]):
                    a = fishbowl[i][j]
                    b = fishbowl[ni][nj]
                    d = abs(a - b) // 5

                    if d > 0:
                        if a > b:
                            new_arr[i][j] -= d
                            new_arr[ni][nj] += d
                        else:
                            new_arr[i][j] += d
                            new_arr[ni][nj] -= d

    fishbowl = new_arr


# 2차원 배열 -> 1차원 배열
def flatten_fishbowl():
    global fishbowl

    result = []
    max_width = max(len(row) for row in fishbowl)

    # 아래에서 위로
    for x in range(max_width):
        for y in range(len(fishbowl) - 1, -1, -1):
            if x < len(fishbowl[y]):
                result.append(fishbowl[y][x])

    fishbowl = result


def rotate_180(arr):
    return [row[::-1] for row in arr[::-1]]


# 1차원 배열 -> 2차원 배열
def update_fishbowl_half():
    global fishbowl
    # 이 함수가 호출될 땐 항상 1차원 배열

    # 1번 공중부양: 왼쪽 N/2개를 뒤집어서 오른쪽 위에
    left = fishbowl[:N//2]
    right = fishbowl[N//2:]

    fishbowl = [left[::-1], right]

    # 2번 공중부양: 왼쪽 N/4열(2행짜리 블록)을 180도 회전해서 오른쪽 위에
    left_block = [row[:N//4] for row in fishbowl]
    right_block = [row[N//4:] for row in fishbowl]

    left_block = rotate_180(left_block)

    # 완성된 건 2차원 배열
    fishbowl = left_block + right_block



N, K = map(int, input().split())
fishbowl = list(map(int, input().split()))
ans = 0

while max(fishbowl) - min(fishbowl) > K:
    ans += 1

    # 1. 물고기 수가 가장 작은 어항에 물고기를 한 마리씩 넣는다
    add_fish_first()

    # 2. 어항 쌓기
    update_fishbowl()

    # 3. 물고기 수 조절
    adjust_fish_num()

    # 4. 어항 일렬로 둔다
    flatten_fishbowl()

    # 5. 공중부양 작업 2번
    update_fishbowl_half()

    # 6. 물고기 수 조절
    adjust_fish_num()

    # 7. 일렬로 둔다
    flatten_fishbowl()

print(ans)

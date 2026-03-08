import sys
from collections import deque

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, sys.stdin.readline().split())
arr_winter_fert = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 각 칸에 추가되는 양분의 양

arr_fert = [[5] * N for _ in range(N)]
tree_dict = dict()

# 나무 자료구조에 나무들을 넣는다.
for _ in range(M):
    y, x, age = map(int, sys.stdin.readline().split())

    # 0-indexed 로 변환
    y -= 1
    x -= 1
    # 그 키가 없으면
    if tree_dict.get((y, x), -1) == -1:
        tree_dict[(y, x)] = []
    tree_dict[(y, x)].append(age)

# 나무들을 나이 적은 순으로 정렬 후 deque로 변환
for y, x in tree_dict.keys():
    tree_dict[(y, x)].sort()
    tree_dict[(y, x)] = deque(tree_dict[(y, x)])

######### K년 반복 ########
for _ in range(K):
    if len(tree_dict) == 0:
        break

    grow_tree_dict = dict()  # (y, x)  # 이걸 딕셔너리로 바꾸면?
    deleted_key_lst = []  # (y, x)

    # print("start of year")
    # 1. 봄
    for y, x in tree_dict.keys():
        new_tree_lst = deque()  # y, x 에 있는 트리들의 리스트(나이 어린 순으로)

        # 나이 적은 애부터 본다.
        is_dead = False
        dead_fert = 0

        # 인덱스 접근 대신 deque 직접 순회 -> 시간복잡도 차이가 꽤 난다고 함
        for age in tree_dict[(y, x)]:
            # 양분을 먹을 수 있다면?
            if not is_dead and arr_fert[y][x] >= age:
                # 양분은 그만큼 줄고, 나이가 1 증가된다.
                arr_fert[y][x] -= age
                age += 1
                new_tree_lst.append(age)

                # 이때, 만약 나이가 5배수가 됐다면 가을에 번식할 나무 리스트에 추가
                if age % 5 == 0:
                    grow_tree_dict[(y, x)] = grow_tree_dict.get((y, x), 0) + 1

            # 양분을 먹을 수 없다면 트리 리스트에 추가 안 하고, 죽은 나무 리스트에 넣는다
            # 나무 나이 적은 순으로 양분을 먹는다면, 그 뒤는 더 볼 필요 없다.
            else:
                # 아래가 부담되는듯
                # dead_tree_lst.extend([y, x, val] for val in tree_dict[(y, x)][age_idx:])

                # 그냥 여기서 여름 연산
                is_dead = True
                dead_fert += age // 2

        # 여름 양분 즉시 추가
        arr_fert[y][x] += dead_fert

        # 만약 살아남은 나무가 없다면? 그 키도 제거
        if not new_tree_lst:
            deleted_key_lst.append((y, x))

        else:
            tree_dict[(y, x)] = new_tree_lst

    # 다 탐색했으니까 없앨 키 없앤다.
    for y, x in deleted_key_lst:
        tree_dict.pop((y, x))  # 이거 맞는지 확인 -> 맞네

    # print("end of spring")
    # print("end of summer")

    # 3. 가을    (나무 번식)
    for y, x in grow_tree_dict.keys():
        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]

            # 범위밖이면 안됨
            if not (0 <= ny < N and 0 <= nx < N):
                continue

            if tree_dict.get((ny, nx), -1) == -1:
                tree_dict[(ny, nx)] = deque()

            tree_dict[(ny, nx)].extendleft([1] * grow_tree_dict[(y, x)])

    # print("end of autumn")

    # 4. 겨울
    for i in range(N):
        for j in range(N):
            arr_fert[i][j] += arr_winter_fert[i][j]

    # print("end of winter")

####### 루프 끝 #########

# 정답 도출
ans = 0
for y, x in tree_dict.keys():
    ans += len(tree_dict[(y, x)])

print(ans)

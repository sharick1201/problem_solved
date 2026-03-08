"""
나무 재테크

출력: K년이 지난 후 "살아남은 나무의 수"

처음에 양분은 모든 칸에 5만큼 들어있다

M개의 나무를 심을 거임
- 같은 칸에 여러 개의 나무가 심어져 있을 수도 있음

1. 봄      (나무들이 양분을 먹어서, 나이 증가)
- 나무들이 자신의 나이만큼 양분을 먹고, 나이 1 증가
- 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
- 만약 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는, 양분을 먹지 못하고 즉시 죽는다.

=> 나무를 정렬해줘야됨.

2. 여름    (죽은 나무 -> 양분)
- 봄에 죽은 나무가 양분으로 변한다.
- 각 죽은 나무의 나이 // 2 를 그 칸에 양분으로 추가

3. 가을    (나무 번식)
- 나이가 5의 배수인 나무들이 번식한다.
    => 이 나무들에 대하여, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
    => 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

4. 겨울    (양분 추가)
- 각 칸에 추가되는 양분의 양은 A[r][c]

#################################################################
# 구상
#
# 현재 양분 arr_fert[][]
# 나무들 tree_dict = dictionary로 관리
#     - 키 : (y, x)
#     - val : [나이]
#
# 죽은 나무들 dead_tree_lst = []   (y, x, age)
# 나이가 5배수인 나무들 grow_tree_lst = []    (y, x)
# ########################################################
#
# 처음에 dict에 넣어두고, 각 val을 내림차순으로 정렬 (reverse = True)
#     - 이후에는 안해줘도 됨. 못 먹는 나무들이 죽어도 내림차순으로 정렬된 상태고,
#       가을에 나이가 가장 어린 1인 나무만 들어오니까 맨 마지막에 append
#
# #### 각 루프마다
#
# dead_tree_lst = []
# grow_tree_lst = []
#
# 1. 봄
# - 나무들이 자신의 나이만큼 양분을 먹고, 나이 1 증가
# - 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
# - 만약 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는, 양분을 먹지 못하고 즉시 죽는다.
# for y, x in dict.key():
#
#     # 그 자리에 양분이 없는 경우는 없다.... 적어도 1은 있음
#
#     # y, x 에 있는 트리들의 리스트(나이 많은 순)
#     new_tree_lst = tree_dict[y][x][:]
#     for age in tree_dict[y][x]:
#
#         # 양분을 먹을 수 있다면?
#         if arr_fert[y][x] >= age:
#             # 양분을 먹고, 나이가 1 증가된다.
#             arr_fert[y][x] -= age
#             age += 1
#             new_tree_lst.append((age))
#
#             # 이때, 만약 나이가 5배수가 됐다면 가을에 번식할 나무 리스트에 추가
#             if age % 5 == 0:
#                 grow_tree_lst.append((y, x))
#
#         # 양분을 먹을 수 없다면 트리 리스트에 추가 안 하고, 죽은 나무 리스트에 넣는다
#         else:
#             dead_tree_lst.append((y, x, age))
#
#
# 2. 여름    (죽은 나무 -> 양분)
# - 봄에 죽은 나무가 양분으로 변한다.
# - 각 죽은 나무의 나이 // 2 를 그 칸에 양분으로 추가
# for y, x, age in dead_tree_lst:
#     arr_fert[y][x] += age // 2
#
#
# 3. 가을    (나무 번식)
# - 나이가 5의 배수인 나무들이 번식한다.
#     => 이 나무들에 대하여, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
#     => 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
#
# for y, x in grow_tree_lst:
#     for d in range(8):
#         # 범위밖이면 안됨
#
#         # 그 외는 다 추가
#         # 만약 그 키가 없으면(그 좌표에 나무가 없었으면) -> 키에 빈 리스트 추가한 다음, append
#         # 만약 그 키가 있으면 그냥 그 키.append
#
# 4. 겨울
# for i in range(N):
#     for j in range(N):
#         arr_fert[][] += arr_winter_fert[][]
#
#
# 루프 끝 #####################
#
# # 정답 도출
# ans = 0
# for y, x in tree_dict.key():
#     ans += len(tree_dict[y][x])
#
# print(ans)

"""
# 와미친 나이 많은 순이 아니라 어린 순;;;
# 나이 많은 순으로 정렬해두고, 봄에는 뒤에서부터 순회
# new_lst[::-1] 해서 append 하면 됨 -> 이거 오래 걸리나? 다르게 ㄱㄱ

"""
dict에 deque 까지 넣는 개뇌절자료구조 쓸 리가 없다.. dict로 충분하다고 생각했는데 
뇌절자료구조를쓰는게맞는듯ㅠㅠ 문제수준 개높네
덱 쓰면 순회에 시간이 너무 오래걸리는 줄 알았는데 O(N^2)
인덱스 접근 대신 직접순회하면 그냥 O(N)

엥 또 시간초과 처 남

autumn 에서 나무 증가 로직이 불필요하게 많은 게 문제였음 🚬 ヽ(´з`)y―┛🚬 ヽ(´з`)y―┛🚬 ヽ(´з`)y―┛🚬 ヽ(´з`)y―┛🚬 ヽ(´з`)y―┛
그 외에 다른 곳에서 시간개선하려고 쓴 것도 죄다 필요하고... (없으면 시간초과나는듯)
리스트 컴프리핸션 편하다고 막 썼는데, 얘도 새로운 객체를 생성하는 거기 때문에 부담이 됨 (마상파이어볼에서 temp 배열 쓴거랑 아닌거랑 시간 차이 많이 나는 것처럼)
운수와 능지 모두 참안좋은날이었다... 에 휴 참많이배웠다 ^_^
"""

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


"""
5 6 1
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 4
2 1 1
2 1 8
2 1 7
2 1 9
3 2 3
"""
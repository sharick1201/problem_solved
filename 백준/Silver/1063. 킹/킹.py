'''
8x8

돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동

입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는
그 이동은 건너 뛰고 다음 이동

킹과 돌의 마지막 위치 구하자
킹은 1
돌은 2 로 두자
'''

move = {'R': [0, 1],
        'L': [0, -1],
        'B': [1, 0],
        'T': [-1, 0],
        'RT': [-1, 1],
        'LT': [-1, -1],
        'RB': [1, 1],
        'LB': [1, -1]
        }

king_pos, dol_pos, N = map(str, input().split())

# 킹 자리에 둔다
king_y = 8 - int(king_pos[1])
king_x = ord(king_pos[0]) - ord('A')

# 돌 자리에 둔다
dol_y = 8 - int(dol_pos[1])
dol_x = ord(dol_pos[0]) - ord('A')



# 이동하자
for _ in range(int(N)):
    cmd = input().strip()

    ny = king_y + move[cmd][0]
    nx = king_x + move[cmd][1]

    # 범위 밖이면 그 명령 무시
    if not (0 <= ny < 8 and 0 <= nx < 8):
        continue

    # 가고자 하는 자리에 돌이 있으면
    if dol_y == ny and dol_x == nx:
        # 그 돌도 이동시킨다
        ny_dol = dol_y + move[cmd][0]
        nx_dol = dol_x + move[cmd][1]

        # 근데 그 돌도 이동시킬 수 없다면? 돌도 이동 안 시키고 킹도 이동 안 시킨다
        if not (0 <= ny_dol < 8 and 0 <= nx_dol < 8):
            continue

        # 돌 이동시킬 수 있으면, 킹과 돌을 모두! 이동시킨다
        king_y = ny
        king_x = nx
        dol_y = ny_dol
        dol_x = nx_dol

    # 그 자리에 돌이 없으면
    else:
        king_y = ny
        king_x = nx

# 킹 위치, 돌 위치를 문제에서 요구하는 포맷으로 수정한다.
king_y = 8 - king_y
king_x = chr(king_x + ord('A'))
print(king_x, king_y, sep='')

dol_y = 8 - dol_y
dol_x = chr(dol_x + ord('A'))
print(dol_x, dol_y, sep='')

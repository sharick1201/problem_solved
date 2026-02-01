from collections import deque


def processing_cmd(wheel_idx, direction):
    change = []
    change.append((wheel_idx, direction))

    wheel_idx_for_left = wheel_idx
    wheel_dir_for_left = direction
    wheel_idx_for_right = wheel_idx
    wheel_dir_for_right = direction


    while True:
        # 타겟 톱니바퀴 기준 -1 -> 그 톱니바퀴도 회전할 것인지 체크하고, 회전하면 change에 append
        if wheel_idx_for_left-1 >= 0:
            if wheels[wheel_idx_for_left][6] != wheels[wheel_idx_for_left-1][2]:
                if wheel_dir_for_left == 1:
                    wheel_dir_for_left = -1
                else:    # -1이었으면
                    wheel_dir_for_left = 1

                change.append((wheel_idx_for_left-1, wheel_dir_for_left)) # -1 방향이었으면 1, 1 방향이었으면 -1으로 명령
                wheel_idx_for_left -= 1
            else: # 더 회전 불가
                break
        else: # 인덱스가 -1 되어도 더 볼 거 없음
            break


    while True:
        # 타겟 톱니바퀴 기준 +1
        if wheel_idx_for_right+1 < 4:
            if wheels[wheel_idx_for_right][2] != wheels[wheel_idx_for_right+1][6]:

                if wheel_dir_for_right == 1:
                    wheel_dir_for_right = -1
                else:    # -1이었으면
                    wheel_dir_for_right = 1

                change.append((wheel_idx_for_right+1, wheel_dir_for_right))
                wheel_idx_for_right += 1

            else:
                break

        else:
            break

    # 톱니바퀴 이동시킨다.
    for i in range(len(change)):
        now_wheel_idx, now_direction = change[i]

        if now_direction == 1:
            first_one = wheels[now_wheel_idx].pop(-1)
            wheels[now_wheel_idx].insert(0, first_one)
        else:   # -1 이면
            last_one = wheels[now_wheel_idx].pop(0)
            wheels[now_wheel_idx].append(last_one)


# 톱니바퀴 저장하는 자료구조.
# [0] -> 1번 톱니바퀴
# [0][0] -> 1번 톱니바퀴의 12시방향 톱니 (이후 시계방향 순으로 입력되어 있다.)
# N극이면 0, S극이면 1
wheels = [list(map(int, input())) for _ in range(4)]
cmd_n = int(input())

# 명령들 받고 시뮬레이션 돌린다
for _ in range(cmd_n):
    wheel_num, direction = map(int, input().split())
    processing_cmd(wheel_num - 1, direction)   # 방향이 1이면 시계방향, -1면 반시계방향

# 점수 계산
ans1 = 0 if wheels[0][0] == 0 else 1
ans2 = 0 if wheels[1][0] == 0 else 2
ans3 = 0 if wheels[2][0] == 0 else 4
ans4 = 0 if wheels[3][0] == 0 else 8

print(ans1 + ans2 + ans3 + ans4)
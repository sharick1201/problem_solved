'''
구현까지 35분 + 디버깅 20분

1. 돌릴 수 있는 부분을 모두 돌려보고
2. 모든 면의 색상이 모두 같은지 확인하면 된다

큐브를 어떤 자료구조에 둘 건지?
회전 -> 2칸씩 밀린다

입력값에 비해 메모리가 넉넉하다
각 회전에 필요한 덱 그때그때 만들어서 쓰면 편할듯
'''
from collections import deque

# 큐브 돌려보고, 풀렸는지 체크하는 함수(check_solved) 호출
def rotate_cube_in_two_ways(ord):
    q = deque(ord)

    # 한쪽 90도
    q.rotate(2)
    if check_solved(q, ord):
        print(1)
        exit()

    # 반대편 90도 (위에서 90도 돌린 것 복구 2 + 반대편 90도 2번)
    q.rotate(-4)
    if check_solved(q, ord):
        print(1)
        exit()


# return: 큐브가 풀리는지(모든 면이 동일한 색인지) 확인
def check_solved(q, ord):
    for i in range(1, 25, 4):
        temp = []
        for j in range(i, i+4):
            if j in ord:
                q_idx = ord.index(j)
                temp.append(origin_lst[q[q_idx]])
            else:
                temp.append(origin_lst[j])

        # 한 면의 모든 값이 동일하지 않으면
        if not all(x == temp[0] for x in temp):
            return False

    return True



# i번째 = idx번째가 되도록 [0] 추가
origin_lst = [0] + list(map(int, input().split()))


# 여섯 케이스밖에 없으니까 할만함
# 전개도상 세로 파트를 돌리는 경우
rotate_cube_in_two_ways([1, 3, 5, 7, 9, 11, 24, 22])

rotate_cube_in_two_ways([2, 4, 6, 8, 10, 12, 23, 21])

# 전개도상 가로 파트를 돌리는 경우
rotate_cube_in_two_ways([13, 14, 5, 6, 17, 18, 21, 22])

rotate_cube_in_two_ways([15, 16, 7, 8, 19, 20, 23, 24])

# 그.. 뭐라해야하지 허리부분? 을 돌리는 경우
rotate_cube_in_two_ways([3, 4, 17, 19, 10, 9, 16, 14])

rotate_cube_in_two_ways([1, 2, 18, 20, 12, 11, 15, 13])

# 여기까지 왔는데 큐브 못 풀었다?
print(0)
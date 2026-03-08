"""
개미굴을 트라이로 만들면 됨
트라이는 딕셔너리로 만들면 됨
"""
# 개미굴 출력
def print_cave(cur_level, depth):
    # 키들 정렬 후 탐색
    for food in sorted(cur_level.keys()):
        # 단위작업
        print("--" * depth + food)
        # 재귀호출
        print_cave(cur_level[food], depth + 1)


N = int(input())
ant_cave = {}

# 개미굴 구조 만들기
for _ in range(N):
    K, *path = list(input().split())
    K = int(K)

    cur_level = ant_cave
    for food in path:
        # 그 먹이가 현재 층에 없으면, 새 딕셔너리 생성
        if food not in cur_level:
            cur_level[food] = {}
        # 다음 층으로 ㄱㄱ
        cur_level = cur_level[food]

print_cave(ant_cave, 0)
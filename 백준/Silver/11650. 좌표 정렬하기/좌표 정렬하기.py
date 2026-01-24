N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# 파이썬 sort() 는...
# 리스트의 요소가 튜플인 경우,
# 튜플의 첫 번째 요소를 기준으로 정렬하고,
# 첫 번째 요소가 같은 경우 두 번째 요소를 기준으로 정렬한다고 한다!!! 이걸해주네
points.sort()

for point in points:
    print(point[0], point[1])
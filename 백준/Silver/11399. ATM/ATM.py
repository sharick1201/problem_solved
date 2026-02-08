N = int(input())
lst = list(map(int, input().split()))

lst.sort()

total_time = 0 # 총 시간
accumulate = 0 # 각 사람이 걸리는 시간

for time in lst:
    accumulate += time
    total_time += accumulate

print(total_time)

nums = []

for _ in range(9):
    num = int(input())
    nums.append(num)

mval = max(nums)
midx = nums.index(mval) + 1

# 결과를 출력합니다.
print(mval)
print(midx)

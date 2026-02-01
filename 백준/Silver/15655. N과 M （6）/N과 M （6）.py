def backtracking(start, N, M, seq):
    if len(seq) == M:
        print(*seq)
        return

    for i in range(start, N):
        seq.append(nums[i])
        backtracking(i + 1, N, M, seq)
        seq.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
backtracking(0, N, M, [])
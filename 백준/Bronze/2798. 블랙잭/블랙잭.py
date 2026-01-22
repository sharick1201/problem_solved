N, M = map(int, input().split())
cards = list(map(int, input().split()))

maxsum = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            cursum = cards[i] + cards[j] + cards[k]
            if cursum <= M:
                maxsum = max(maxsum, cursum)

print(maxsum)
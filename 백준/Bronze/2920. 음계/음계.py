lst = list(map(int, input().split()))
ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]
ans = "ascending"

for i in range(8):
    if lst[i] != ascending[i]:
        ans = "descending"
        break

if ans == "descending":
    for i in range(8):
        if lst[i] != descending[i]:
            ans = "mixed"
            break
print(ans)
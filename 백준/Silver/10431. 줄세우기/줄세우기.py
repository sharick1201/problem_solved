P = int(input())
for _ in range(P):
    lst = list(map(int, input().split()))
    total = 0
    for i in range(1, len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]: 
                lst[i], lst[j] = lst[j], lst[i]
                total += 1
    print(lst[0], total)
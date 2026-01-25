T = int(input())

for _ in range(T):
    txt = input()
    ans = 0
    cnt = 1
    
    for char in txt:
        if char == 'O':
            ans += cnt
            cnt += 1
        else: # char == 'X'
            cnt = 1
    
    print(ans)